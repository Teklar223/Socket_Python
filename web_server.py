# import socket module
from socket import *
import sys  # In order to terminate the program

PORT = 2000
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare the sever socket
serverSocket.bind(("", PORT))
serverSocket.listen(1)  # only 1 connection as per exercise demand

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, address = serverSocket.accept()

    try:
        message = connectionSocket.recv(
            4096).decode()  # receives a message with a max size of 4096 bits and decodes it.
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
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
