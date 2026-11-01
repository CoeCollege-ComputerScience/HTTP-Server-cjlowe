import OOServer
import random
import datetime
from netTools import *

html = """<!DOCTYPE html>
<html>
<head> <title>Simple Server</title>
</head>
<body>
**Content**
</body>
</html>
"""

server = OOServer.Server()


@server.endpoint("/dice/1")
def roll1(query):
    body = "<a href=\"/dice/" + roll() + "\"> <button> Roll Dice </button></a>"
    body += "<img src=RedDie1.png>"
    lightpage = html.replace("**Content**", body)
    return lightpage

@server.endpoint("/dice/2")
def roll2(query):
    body = "<a href=\"/dice/" + roll() + "\"> <button> Roll Dice </button></a>"
    body += "<img src=RedDie2.png>"
    lightpage = html.replace("**Content**", body)
    return lightpage

@server.endpoint("/dice/3")
def roll3(query):
    body = "<a href=\"/dice/" + roll() + "\"> <button> Roll Dice </button></a>"
    body += "<img src=RedDie3.png>"
    lightpage = html.replace("**Content**", body)
    return lightpage

@server.endpoint("/dice/4")
def roll4(query):
    body = "<a href=\"/dice/" + roll() + "\"> <button> Roll Dice </button></a>"
    body += "<img src=RedDie4.png>"
    lightpage = html.replace("**Content**", body)
    return lightpage

@server.endpoint("/dice/5")
def roll5(query):
    body = "<a href=\"/dice/" + roll() + "\"> <button> Roll Dice </button></a>"
    body += "<img src=RedDie5.png>"
    lightpage = html.replace("**Content**", body)
    return lightpage

@server.endpoint("/dice/6")
def roll6(query):
    body = "<a href=\"/dice/" + roll() + "\"> <button> Roll Dice </button></a>"
    body += "<img src=RedDie6.png>"
    lightpage = html.replace("**Content**", body)
    return lightpage

@server.endpoint("/collection/name/get")
def getName(query):
    body = "<form action=\"/collection/nameResult\" method=\"GET\">"
    body += "<label for=\"name\">Name:</label>"
    body += "<input type=\"text\" id=\"name\" name=\"name\">"
    body += "<button type=\"submit\">Submit</button>"
    body += "</form>"

    lightpage = html.replace("**Content**", body)
    return lightpage

@server.endpoint("/collection/name/post")
def getName(query):
    body = "<form action=\"/collection/nameResult\" method=\"POST\">"
    body += "<label for=\"name\">Name:</label>"
    body += "<input type=\"text\" id=\"name\" name=\"name\">"
    body += "<button type=\"submit\">Submit</button>"
    body += "</form>"

    lightpage = html.replace("**Content**", body)
    return lightpage

@server.endpoint("/collection/temp")
def getTemp(query):
    body = "<form action=\"/collection/tempResult\" method=\"GET\">"
    body += "<label for=\"temp\">Current Temperature:</label>"
    body += "<input type=\"text\" id=\"temp\" name=\"temp\">"
    body += "<button type=\"submit\">Submit</button>"
    body += "</form>"

    lightpage = html.replace("**Content**", body)
    return lightpage

@server.endpoint("/collection/tempResult")

@server.endpoint("/collection/nameResult")
def showTame(query):
    print("Given Query: " + query)
    temp = query.split("=")[1]
    body = "<p>Hello, thank you for your assistance!<br>"
    body += "The temperature is currently: " + temp + "</p>"

    lightpage = html.replace("**Content**", body)
    return lightpage

def roll():
    return str(random.randint(1, 6))


server.run()

# def processRequest(s,addr):
#     request = getMessage(s)
#     print("initial request: " + request)
#
#     if request[:3] == "GET":
#         GETHandling(request, s)
#     elif request[:4] == "POST":
#         POSTHandling(request, s)
#     else:
#         response = "Status Code 403 - Forbidden\r\n"
#         response += "\r\n"
#         response += "Invalid Command"
#         s.send(response.encode("utf-8"))

    #response = "Gotcha"
    #s.send(response.encode("utf-8"))
    # s.close()

# def GETHandling(request, s):
#     print("Reached 1")
#     print("Request: " + request)
#     request = request[4:]
#     spaceLoc = request.find(' ')
#     resource = request[:spaceLoc]
#     resource = resource.strip("/")
#     print("resourceGet: " + resource)
#     # resource = "public_html/" + resource
#     innerHandling(resource, s)
#
# def innerHandling(resource, s):
#     info = ""
#     if "?" in resource:
#         splitResource = resource.split("?")
#         resource = splitResource[0]
#         info = splitResource[1]
#         print("beginning info: " + info)
#
#     if resource[-5:].lower() == ".html":
#         try:
#             inFile = open("public_html/" + resource, "r")
#         except FileNotFoundError:
#             response = "Status Code 404 - Not Found\r\n"
#             response += "\r\n"
#             response += "Requested File Not Found In System"
#             s.send(response.encode("utf-8"))
#         else:
#             response = "HTTP/1.0 200 OK\r\n"
#             response += "Content-Type: text/html\r\n"
#             response += "\r\n"
#             response += inFile.read()
#             inFile.close()
#             s.send(response.encode("utf-8"))
#     elif resource[-4:].lower() == ".jpg":
#         rbHandling(resource, "jpeg", s)
#     elif resource[-4:].lower() == ".bmp":
#         rbHandling(resource, "bmp", s)
#     elif resource[-4:].lower() == ".png":
#         rbHandling(resource, "png", s)
#     elif resource[-4:].lower() == ".gif":
#         rbHandling(resource, "gif", s)
#     elif resource[-4:].lower() == ".ico":
#         rbHandling(resource, "x-icon", s)
#     elif resource[-4:].lower() == ".pdf":
#         rbHandling(resource, "pdf", s)
#     elif resource[-3:].lower() == ".ss":
#         s.send(ssHandling(resource, info).encode('utf-8'))
#     else:
#         response = "Status Code 403 - Forbidden\r\n"
#         response += "\r\n"
#         response += "Invalid Command"
#         s.send(response.encode("utf-8"))
#
# def POSTHandling(request, s):
#     print("Request: " + request + "\n+++++++\n")
#     request = request[5:]
#     check = request.find("\r\n\r\n")
#     mainInfo = request[check:].strip()
#     print("Main Info: " + mainInfo)
#     spaceLoc = request.find(' ')
#     resource = request[:spaceLoc]
#     resource = resource.strip("/")
#     print("resourcePost: " + resource)
#     resource += "?" + mainInfo
#     print("Resource sent out: " + resource)
#     innerHandling(resource, s)
#
# def rbHandling(resource, code, s):
#     try:
#         inFile = open("public_html/" + resource, "rb")
#     except FileNotFoundError:
#         response = "Status Code 404 - Not Found\r\n"
#         response += "\r\n"
#         response += "Requested File Not Found In System"
#         s.send(response.encode("utf-8"))
#     else:
#         response = "HTTP/1.0 200 OK\r\n"
#         response += "Content-Type: image/" + code + "\r\n"
#         response += "\r\n"
#         s.send(response.encode("utf-8"))
#
#         s.send(inFile.read())
#         inFile.close()
#
# def ssHandling(resource, info):
#     # request example
#     # Greeting.ss?fname=Colton&lname=Lowe
#     response = "HTTP/1.0 200 OK\r\n"
#     response += "Content-Type: text/html\r\n"
#     response += "\r\n"
#     print("resource at ss handling: " + resource)
#     # creating file skeleton
#     with open("public_html/template.html", "r") as inFile:
#         template = inFile.read()
#     title = resource.split(".")[0]
#     print("Title: " + title)
#     skeleton = template.replace("{{TITLE}}", title)
#     if title == "Time":
#         now = datetime.now()
#         now = now.strftime("%H:%M:%S")
#         skeleton = skeleton.replace("{{BODY}}", now)
#     # example message
#     # http://localhost:63342/Greeting.ss?fname=Colton&lname=Lowe
#     elif title == "Greeting":
#         print("info: " + info)
#         info = info.split("&")
#         fname = (info[0].split("="))[1]
#         lname = (info[1].split("="))[1]
#         skeleton = skeleton.replace("{{BODY}}", ("Hello " + fname + " " + lname))
#     elif title == "Vote":
#         voteTarget = info[7:]
#         updateRecord(voteTarget)
#         skeleton = skeleton.replace("{{BODY}}", ("Thank you for voting!<br>You voted for the " + voteTarget + "<br>Total Vote Scores:<br>" + votingRecords()))
#         #example
#         #http://localhost:63342/Vote.ss?ballet=Rutabagas
#     print("skeleton: " + skeleton)
#     response += skeleton
#     print("response: " + response)
#     return response

def votingRecords(): #working
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

def updateRecord(party): #not working
    selectedIndex = -1
    newNumber = 0
    with open("VotingRecords.txt", "r") as file:
        lines = file.readlines()
    print("party: " + party)
    index = 0
    for line in lines:
        print("party: " + party)
        print("line: " + line)
        if line.strip("\n") == party:
            selectedIndex = index + 1
            newNumber = int(lines[selectedIndex]) + 1
            print("Selected Index to change: " + str(selectedIndex))
        index += 1
    #now rewriting
    with open("VotingRecords.txt", "w") as f:
        i = 0
        for line in lines:
            print("iterated")
            if i == selectedIndex:
                f.write(str(newNumber) + "\n")
            else:
                f.write(str(lines[i]))
            i += 1

# def SimpleServer():
#     serversocket = socket()
#     # host = "172.16.212.120"
#     # host = "192.168.12.52"
#     host = "192.168.0.140"
#     print("Listening on: ", host, ":8002")
#     serversocket.bind((host, 8002))
#     serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#     serversocket.listen()
#
#     while True:
#         print("Waiting for connection....")
#         clientsocket, addr = serversocket.accept()
#
#         print("Connnection from", addr)
#         threading.Thread(target=processRequest, args=(clientsocket,addr)).start()
#
#
# SimpleServer()


#------------------------------------------------------------------#

