from netTools import *
import threading
from datetime import datetime


def custom_logic_function(username, email):
    # Process your data here
    print(f"Executing function with Username: {username}, Email: {email}")
    return f"<h3>Success!</h3><p>Processed data for {username} ({email})</p>"

def processRequest(s,addr):
    request = getMessage(s)
    print(request)

    if request[:3] == "GET":
        print("Reached 1")
        request = request[4:]
        spaceLoc = request.find(' ')
        resource = request[:spaceLoc]
        resource = resource.strip("/")
        print("resource: " + resource)
        resource = "public_html/" + resource

        if resource[-5:].lower() == ".html":
            try:
                inFile = open(resource, "r")
            except FileNotFoundError:
                response = "Status Code 404 - Not Found\r\n"
                response += "\r\n"
                response += "Requested File Not Found In System"
                s.send(response.encode("utf-8"))
            else:
                response = "HTTP/1.0 200 OK\r\n"
                response += "Content-Type: text/html\r\n"
                response += "\r\n"
                response += inFile.read()
                inFile.close()
                s.send(response.encode("utf-8"))
        elif resource[-4:].lower() == ".jpg":
            rbHandling(resource, "jpeg", s)
        elif resource[-4:].lower() == ".bmp":
            rbHandling(resource, "bmp", s)
        elif resource[-4:].lower() == ".png":
            rbHandling(resource, "png", s)
        elif resource[-4:].lower() == ".gif":
            rbHandling(resource, "gif", s)
        elif resource[-4:].lower() == ".ico":
            rbHandling(resource, "x-icon", s)
        elif resource[-4:].lower() == ".pdf":
            rbHandling(resource, "pdf", s)
        elif resource[-3:].lower() == ".ss":
            s.send(ssHandling(resource).encode('utf-8'))
        else:
            response = "Status Code 403 - Forbidden\r\n"
            response += "\r\n"
            response += "Invalid Command"
            s.send(response.encode("utf-8"))
    elif request[:4] == "POST":
        request = request[4:]
        spaceLoc = request.find(' ')
        resource = request[:spaceLoc]
        resource = resource.strip("/")
        info = ""
        #request example
        #Greeting.ss?fname=Colton&lname=Lowe
        if "?" in resource:
            splitResource = resource.split("?")
            resource = splitResource[0]
            info = splitResource
        print("resource: " + resource)
        resource = "public_html/" + resource

        if resource[-3:].lower() == ".ss":
            s.send(ssHandling(resource).encode('utf-8'))
    else:
        response = "Status Code 403 - Forbidden\r\n"
        response += "\r\n"
        response += "Invalid Command"
        s.send(response.encode("utf-8"))

    #response = "Gotcha"
    #s.send(response.encode("utf-8"))
    s.close()


def rbHandling(resource, code, s):
    try:
        inFile = open(resource, "rb")
    except FileNotFoundError:
        response = "Status Code 404 - Not Found\r\n"
        response += "\r\n"
        response += "Requested File Not Found In System"
        s.send(response.encode("utf-8"))
    else:
        response = "HTTP/1.0 200 OK\r\n"
        response += "Content-Type: image/" + code + "\r\n"
        response += "\r\n"
        s.send(response.encode("utf-8"))

        s.send(inFile.read())
        inFile.close()
        print(inFile.read())

def ssHandling(resource):
    info = ""
    # request example
    # Greeting.ss?fname=Colton&lname=Lowe
    if "?" in resource:
        splitResource = resource.split("?")
        resource = splitResource[0]
        info = splitResource[1]
    response = "HTTP/1.0 200 OK\r\n"
    response += "Content-Type: text/ss\r\n"
    response += "\r\n"
    # creating file skeleton
    with open("public_html/template.html", "r") as inFile:
        template = inFile.read()
    title = resource.split("/")[-1][:-3]
    skeleton = template.replace("{{TITLE}}", title)
    if title == "Time":
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        skeleton = skeleton.replace("{{BODY}}", now)
    # example message
    # http://localhost:63342/Greeting.ss?fname=Colton&lname=Lowe
    elif title == "Greeting":
        info = info.split("&")
        skeleton = skeleton.replace("{{BODY}}", ("Hello " + (info[0])[6:] + " " + (info[1])[6:]))
    elif title == "Vote":
        voteTarget = info[7:]
        updateRecord(voteTarget)
        skeleton = skeleton.replace("{{BODY}}", ("Thank you for voting!<br>You voted for the " + voteTarget + "<br>Total Vote Scores:<br>" + votingRecords()))
        #example
        #http://localhost:63342/Vote.ss?ballet=Rutabagas
    response += skeleton
    return response

def votingRecords():
    with open("VotingRecords.txt", "r") as file:
        lines = file.readlines()

    totalText = ""
    index = 0
    for line in lines:
        if index % 2 == 0:
            totalText += line + " Votes: "
        else:
            totalText += line + "<br>"
        index += 1
    return totalText

def updateRecord(party):
    selectedIndex = -1
    with open("VotingRecords.txt", "r") as file:
        lines = file.readlines()
    if party in lines:
        index = 0
        for line in lines:
            if line == party:
                selectedIndex = index + 1
            index += 1
    #now rewriting
    with open("VotingRecords.txt", "w") as file:
        index = 0
        for line in lines:
            if index == selectedIndex:
                file.write(str(int(lines[selectedIndex]) + 1))
            else:
                file.write(lines[index])
            index += 1

def SimpleServer():
    serversocket = socket()
    # host = "172.16.212.120"
    # host = "192.168.12.52"
    host = "192.168.0.140"
    print("Listening on: ", host, ":8002")
    serversocket.bind((host, 8002))
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversocket.listen()

    while True:
        print("Waiting for connection....")
        clientsocket, addr = serversocket.accept()

        print("Connnection from", addr)
        threading.Thread(target=processRequest, args=(clientsocket,addr)).start()


SimpleServer()