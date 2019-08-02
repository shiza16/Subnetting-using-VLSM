from socket import *
import time
import ipaddress
import subprocess
from ipaddress import IPv4Address, IPv4Network, IPv4Interface
import socket

serverPort1 = 12001
serverSocket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket1.bind(('' ,serverPort1))

serverSocket1.listen(1)
print ("The server is ready to receive")

while True:
    
    
    connectionSocket1 , addr = serverSocket1.accept()
    ipadd = connectionSocket1.recv(1024).decode()
    noOfhosts = connectionSocket1.recv(1024)
    noOfSubnet = connectionSocket1.recv(1024)
    print(ipadd)
    x=ipaddress.ip_network(ipadd)
    print(x)
    noOfhosts = int(noOfhosts)
    #Calculates new prefix here based on input from client
    noOfSubnet = int(noOfSubnet)
    currentprefix = x.prefixlen 
    count = 0
    count1 = 0
    a = 1
    b=1
    newprefix = 0
    
    while a < noOfSubnet:
        a = a*2
        count+=1
    
    newprefix = currentprefix + count 
    print ("Count " + str(count))
    print ("Current Prefix " + str(currentprefix))
    print ("New Prefix " + str(newprefix))
    if newprefix <= 32:
        while b < noOfhosts:
            b = b*2
            count1 += 1
    newprefix1  = newprefix + count1
    if newprefix1 > 32:
        print ('Prefix with Hosts: ' + str(newprefix1))
        print ('Cannot be subnetted')
        connectionSocket1.send("Cannot be subnetted")
        connectionSocket.close()
        connectionSocket1.close()
        exit()
        
  
    s1=list(x.subnets(new_prefix=newprefix))
    print(noOfhosts)
    print(noOfSubnet)
    print("No of Networks: " + str(len(s1)))
    connectionSocket1.send("No of Networks: " + str(len(s1)) + "\n")
    for s in s1:
        connectionSocket1.send(str(s.with_netmask)+ '\n')
    for s in s1:
        connectionSocket1.send("\n\n")
        x=ipaddress.ip_network(s.with_netmask)
        connectionSocket1.send("No of possible Hosts per subnet: " + str(len(list(x.hosts()))) + "\n")
        for x1 in x.hosts():
            a=str(x1)
            connectionSocket1.send(a + "\n")

    
    print(x.num_addresses)
    print(x.network_address)
 
    
    connectionSocket.close()
    connectionSocket1.close()

