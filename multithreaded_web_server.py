# since this has not yet been covered in class I looked at these resources:
# 1. https://stackoverflow.com/questions/14088294/multithreaded-web-server-in-python
# 2. https://gist.github.com/gnilchee/246474141cbe588eb9fb
# together they both contain several implementations which are quite different from each other (for reference)

import sys
from socket import *
from threading import *

PORT = 2000  # pre-determined, arbitrary port

serverSocket = socket(AF_INET, SOCK_STREAM)  # defining a TCP socket
serverSocket.listen(10)  # 10 threads for listening

print("Ready to serve on port " + PORT)


def Threader(connection: socket, addr):
    while True:
        try:
            message = connection.recv(4096).decode()
            # message = connectionSocket.recv(4096).decode()
            filename = message.split()[1]
            f = open(filename[1:])
            output_data = f.read()
            # Send one HTTP header line into socket
            response = "HTTP/1.1 200 OK\n\n"
            connectionSocket.send(response.encode())
            print("attempting to send message:" + response)
            # Send the content of the requested file to the client
            for i in range(0, len(output_data)):
                connectionSocket.send(output_data[i].encode())
            connectionSocket.send("\r\n".encode())
            print("message sent!")
            connectionSocket.close()
            break
        except IOError:
            # Send response message for file not found
            connectionSocket.send("HTTP/1.1 404 Not Found\n\n".encode())
            connectionSocket.send("<html><head></head><body><h1>Error 404 Not Found</h1></body></html>\r\n".encode())
            # Close client socket
            connectionSocket.close()
            break


while True:
    try:
        connectionSocket, address = serverSocket.accept()
        print("Connection from " + address)
        thread = Thread(target=Threader, args=(connectionSocket, address))
        thread.start()

    except OSError:
        print("Something went wrong before threading the request!, the run will now stop.\n")
        break

serverSocket.close()
sys.exit()
