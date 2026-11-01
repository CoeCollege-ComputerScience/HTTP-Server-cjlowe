from socket import *
from netTools import *
import threading
html = """<!DOCTYPE html>
<html>
<head> <title>Simple Server</title>
</head>
<body>
**Content**
</body>
</html>
"""
class Server:
    addr = "192.168.12.52"
    def __init__(self):
        self.host = getIPAddress()
        self.port = 8080
        self.functionMap = {}
    def endpoint(self,path):
        print("adding: " +path)
        def inner(func):
            self.functionMap[path] = func
            return func
        return inner
    def run(self):
        # Open socket
        serversocket = socket()
        serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        print("Listening on: ", self.host, ":", self.port)
        serversocket.bind((self.host, self.port))
        serversocket.listen()
        while True:
            print("Waiting for connection....")
            clientsocket, addr = serversocket.accept()
            print("Connnection from", addr)
            threading.Thread(target=self.processRequest,
            args=(clientsocket,)).start()
        serversocket.close()
    def processRequest(self, cl):
        request = getMessage(cl)
        print("*" * 50, "\nNew Request\n", "*" * 50)
        resource = request.split(" ")[1]
        everything = request.split("\r\n\r\n")
        for item in everything:
            print('Item: ' + item)
        print(resource)
        if request[:3] == "GET":
            print("GET: " + resource)
        elif request[:4] == "POST":
            resource += "?" + request.split("\r\n\r\n")[1]
            print("POST: " + resource)
        if resource == "/":
            homePage = html.replace("**Content**", "<h1> OO Server </h1>")
            self.respondHTML(homePage, cl)
        elif resource[-4:].lower() == "html":
            try:
                with open(resource, "r") as inFile:
                    response = inFile.read()
                    self.respondHTML(response, cl)
            except FileNotFoundError:
                self.respondNotFound(cl)
        elif resource[-3:].lower() == "png":
            self.respondImg(resource, cl)
        else:
            try:
                if (request[:3] == "GET"):
                    resource = request.split(" ")[1]
                    print("resource here: " + resource)
                if "?" in resource:
                    path, query = resource.split("?", 1)
                    print("path: " + path)
                    print("query: " + query)
                else:
                    path = resource
                    query = ""

                response = self.functionMap[path](query)
                self.respondHTML(response, cl)
            except KeyError:
                print("not allowed")
                self.respondNotFound(cl)
    def respondHTML(self, body, cl):
        header = 'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n'
        sendMessage(cl, header)
        sendMessage(cl, body)
        cl.close()
    def respondImg(self, resource, cl):
        header = "HTTP/1.0 200 OK\r\n"
        header += "Content-Type: image/png\r\n"
        header += "\r\n"
        try:
            resource = "Image" + resource
            print("Resource: \n", resource)
            infile = open(resource, "rb")
            data = infile.read()
            infile.close()
            sendMessage(cl, header)
            cl.send(data)
            cl.close()
            print("Sent")
        except FileNotFoundError:
            print("bosh", resource)
            self.respondNotFound(cl)

    def respondNotFound(self,cl):
        header = "HTTP/1.0 404 NOT FOUND\r\n\r\n"
        body = homePage = html.replace("**Content**", "<h1> NOT FOUND </h1>")
        sendMessage(cl, header)
        sendMessage(cl, body)
        cl.close()
        print("Not Found")
    #=====================================================