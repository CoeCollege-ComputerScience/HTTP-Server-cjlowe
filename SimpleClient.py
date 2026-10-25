from netTools import *


def SimpleBrowser(ip, resource):
    s = socket()
    s.connect((ip, 8002))
    msg = "GET "+ resource + " HTTP/1.0\r\n"
    msg += "\r\n"
    msg = msg.encode("utf-8")

    s.send(msg)
    response = s.recv(1024)
    data = b""
    while response:
        data += response
        response = s.recv(1024)
    s.close()

    print(data)

#SimpleBrowser("httpbin.org","/#/Anything")

