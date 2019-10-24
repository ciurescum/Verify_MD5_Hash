# Verify_MD5_Hash

**Purpose**

The purpose of this project is to find a hexadecimal seed which can be concatenated with a given string and become an MD5 Hash. The hash has to start with a n number of 0s (n is chosen by the user). 
The project consists of a communication between a server and many clients. The server has to generate a random seed and the n number which will be sent to the clients. Then the clients have to apply a md5 funciton to "seed | string" and check the given condition. If the condition is True, the client sends a message to the server with the number of tries,the found seed and some acknoledge messages. 
The first client who finds the solution will send a shutdown command to the server and will stop the communication with the other clients.


**Instructions**

Start the serve using: python server.py 2 ab5  
Start the client using: python client.py 127.0.0.1
