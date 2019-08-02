An application to design subnets as per  organization requirement

Introduction 

Subnetting is the known as the practice of dividing a Network into Multiple networks to create segregated / separated zones for operations. Subnetting is very handy when you have different zones or departments in an organization to segregate access limited to a specific area. It also allows a company to save costs in terms of deployment by logically segregating networks rather than employing different physical networks.

Description of the project

The project is about an application that implements subnetting. Every organization has multi networks and assigning IP to every network and its sub networks is a task. Subnetting is a technique that easily and logically assigns IPs to the network based upon the requirement of the organization. Common advantages of subnetting include enhancing routing efficiency, network management control and improving network security.
Our project implements this technique. The user is asked about the number of subnets needed by the organization along with hosts needed in each subnet. The network address will be given by the user along with the default subnet mask. We have a client server architecture where the client enters the input and sends it to server side and the server then calculates the subnets and the possible number of hosts per subnet and responds back to client with all the relevant IP addresses. The subnetting is performed based on the number of required networks. No of hosts required are taken just to ensure that enough hosts are available based on the bits available after the new prefix is calculated. The project is coded on python utilizing all the libraries needed to implement the concept of subnetting. TCP connection is established between the client and server before sending the request by the user. 

Pre-requisites for execution of code:

Python socket module 
Python IP address module
Server shall be run before the client to ensure connection has not refused


Input and Output format:

Input:

Input ip add with prefix : <IP>
Input no of hosts: <No of Hosts Required>
Input no of networks: <No of Networks Required>

Output:

No of Networks: <No of Subnets created>
<Subnet Address 1 / Subnet Mask>
<Subnet Address 2 / Subnet Mask>
.
.

No of Host Addresses per subnet: <No of hosts per subnet>
<Host Address 1>
<Host Address 2>
.
.
.
.


Test cases:

Class C:

Input ip add with prefix : 192.168.0.0/24
Input no of hosts: 8
Input no of networks: 16

Class B:

Input ip add with prefix : 172.16.0.0/16
Input no of hosts: 72
Input no of networks: 32


Class A:

Input ip add with prefix : 10.0.0.0/8
Input no of hosts: 1024
Input no of networks: 64


Out of Bounds test case:

Input ip add with prefix : 192.168.0.0/24
Input no of hosts: 256
Input no of networks: 16
