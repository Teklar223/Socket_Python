from socket import *
import sys

# this matches the web_server.py file and uses the port specified there,
# in this version neither port nor the server address are dynamic and
# 'localhost' is a shorthand for the IP specified in said file.
address = ('localhost', 2000)

filename = "." + sys.argv[1]  # this is a user input and treated as a string

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)  # declaring a TCP socket
    clientSocket.connect(address)
    print("connection success!")
    clientSocket.send(("/ " + filename).encode())  # for example when message = "HelloWorld.html"
    response = (clientSocket.recv(4096)).decode()
    print("Received:\n" + response)

except IOError:
    print("Something went wrong, please try again, \r\n (client connection closed!)")
    sys.exit(1)

clientSocket.close()
