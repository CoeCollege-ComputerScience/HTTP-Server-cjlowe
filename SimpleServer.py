from netTools import *
import threading

def processRequest(s,addr):
    request = getMessage(s)
    print(request)

    if request[:3] == "GET":
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
            try:
                inFile = open(resource, "rb")
            except FileNotFoundError:
                response = "Status Code 404 - Not Found\r\n"
                response += "\r\n"
                response += "Requested File Not Found In System"
                s.send(response.encode("utf-8"))
            else:
                response = "HTTP/1.0 200 OK\r\n"
                response += "Content-Type: image/jpeg\r\n"
                response += "\r\n"
                s.send(response.encode("utf-8"))

                s.send(inFile.read())
                inFile.close()
        elif resource[-4:].lower() == ".bmp":
            try:
                inFile = open(resource, "rb")
            except FileNotFoundError:
                response = "Status Code 404 - Not Found\r\n"
                response += "\r\n"
                response += "Requested File Not Found In System"
                s.send(response.encode("utf-8"))
            else:
                response = "HTTP/1.0 200 OK\r\n"
                response += "Content-Type: image/bmp\r\n"
                response += "\r\n"
                s.send(response.encode("utf-8"))

                s.send(inFile.read())
                inFile.close()
        elif resource[-4:].lower() == ".png":
            try:
                inFile = open(resource, "rb")
            except FileNotFoundError:
                response = "Status Code 404 - Not Found\r\n"
                response += "\r\n"
                response += "Requested File Not Found In System"
                s.send(response.encode("utf-8"))
            else:
                response = "HTTP/1.0 200 OK\r\n"
                response += "Content-Type: image/png\r\n"
                response += "\r\n"
                s.send(response.encode("utf-8"))

                s.send(inFile.read())
                inFile.close()
        elif resource[-4:].lower() == ".gif":
            try:
                inFile = open(resource, "rb")
            except FileNotFoundError:
                response = "Status Code 404 - Not Found\r\n"
                response += "\r\n"
                response += "Requested File Not Found In System"
                s.send(response.encode("utf-8"))
            else:
                response = "HTTP/1.0 200 OK\r\n"
                response += "Content-Type: image/gif\r\n"
                response += "\r\n"
                s.send(response.encode("utf-8"))

                s.send(inFile.read())
                inFile.close()
        elif resource[-4:].lower() == ".ico":
            try:
                inFile = open(resource, "rb")
            except FileNotFoundError:
                response = "Status Code 404 - Not Found\r\n"
                response += "\r\n"
                response += "Requested File Not Found In System"
                s.send(response.encode("utf-8"))
            else:
                response = "HTTP/1.0 200 OK\r\n"
                response += "Content-Type: image/x-icon\r\n"
                response += "\r\n"
                s.send(response.encode("utf-8"))

                s.send(inFile.read())
                inFile.close()
                print(inFile.read())
        elif resource[-4:].lower() == ".pdf":
            print("reached pdf")
            try:
                inFile = open(resource, "rb")
            except FileNotFoundError:
                response = "Status Code 404 - Not Found\r\n"
                response += "\r\n"
                response += "Requested File Not Found In System"
                s.send(response.encode("utf-8"))
            else:
                response = "HTTP/1.0 200 OK\r\n"
                response += "Content-Type: image/pdf\r\n"
                response += "\r\n"
                s.send(response.encode("utf-8"))

                s.send(inFile.read())
                inFile.close()
                print(inFile.read())
        else:
            response = "Status Code 403 - Forbidden\r\n"
            response += "\r\n"
            response += "Invalid Command"
            s.send(response.encode("utf-8"))
    else:
        response = "Status Code 403 - Forbidden\r\n"
        response += "\r\n"
        response += "Invalid Command"
        s.send(response.encode("utf-8"))

    #response = "Gotcha"
    #s.send(response.encode("utf-8"))
    s.close()


def SimpleServer():
    serversocket = socket()
    host = "172.16.212.120"
    print("Listening on: ", host, ":8000")
    serversocket.bind((host, 8002))
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversocket.listen()

    while True:
        print("Waiting for connection....")
        clientsocket, addr = serversocket.accept()

        print("Connnection from", addr)
        threading.Thread(target=processRequest, args=(clientsocket,addr)).start()

    serversocket.close()


SimpleServer()
