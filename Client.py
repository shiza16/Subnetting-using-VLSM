
from socket import*
import time 
import socket


serverName = ''
serverPort = 12000
serverPort1 = 12001

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

clientSocket1 = socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket1.connect((serverName,serverPort1))
ipadd= input("Input ip add with prefix : ")
clientSocket.send(ipadd .encode())
requiredClients = input("Input no of hosts: ")
clientSocket.send(requiredClients .encode())


requiredNetworks = input("Input no of networks: ")
clientSocket.send(requiredNetworks .encode())
while(True): 
    data = clientSocket1.recv(4096)
    print (data)
    if data == "Cannot be subnetted":
        exit()
    if not data: break
clientSocket.close();
clientSocket1.close();
