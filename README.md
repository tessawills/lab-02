# Lab 2
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Tessa Wills
- Caroline Dworken

## Lab Question Answers


Question 1: How did the reliability of UDP change when you added 50% loss to your local
environment? Why did this occur?

When forcing a 50% loss on my environment, about half the time the messages would send to the other server, and the other half they would not send at all. When they did send they were received right away, if they did not send, they were never received. So the speed isn't necessarily affected, but the sending and receiving of messages is. This occurred because we forced less reliability on the environment, and since UDP is susceptible to data loss, when forcing less reliability, more data loss occurred.

Question 2: How did the reliability of TCP change? Why did this occur?

All messages sent were received by the server, but the speed varied between messages depending on which ones were affected by the loss. This is because TCP has many more checks and reliability features than UDP, so it was able to recover the messages and receive them properly. 

Question 3: How did the speed of the TCP response change? Why might this happen?

In about half of the messages sent, the time it took for the server to receive the message was much longer than usual, however it still got all of the messages. This might happen because these messages were impacted by the 50% loss we added, so it takes more time for TCP to recover the proper message through its checks. 


1. What is argc and *argv[]?
Info from: https://www.tutorialspoint.com/cprogramming/c_command_line_arguments.htm 

These two variables pass the necessary information for the arguments passed to main(). Argc is the number of arguments passed to main(), and *argv[] is a pointer array with the pointers pointed to each argument passed. 

2. What is a UNIX file descriptor and file descriptor table?
Info from: https://stackoverflow.com/questions/5256599/what-are-file-descriptors-explained-in-simple-terms 
A file descriptor is an integer value that is assigned to each file opened in the OS, so five opened files means we will have five file descriptors (1,2,3,4,5). A file descriptor table stores these file descriptors as well as pointers to the corresponding files themselves, and file descriptor flags. 

3. What is a struct? What's the structure of sockaddr_in?
https://www.w3schools.com/c/c_structs.php 

A struct is similar to an array in that it groups many variables in a single place. The difference is that a struct can store variables of many different types (like char, int, float, etc.) within it. The structure sockaddr_in is a structure meant for server socket connections. Within the struct there will be information on the address family, port number, and IP address of the server. This will allow it to store the address of the server in a specific way for it to be read by a connect function which will create a server connection. 

4. What are the input parameters and return value of socket()

The input parameters are AF_INET , SOCK_STREAM, and 0. AF_INET is the domain parameter that specifies the program is in an internet domain. SOCK_STREAM is the type parameter that specifies that a socket stream is running. 0 is the protocol parameter, in this case when it is set at zero, that means that we are not manually setting the parameter, so it automatically chooses a default parameter that works in this case. 

socket() has a return value that represents the socket file director, so it is an integer greater than or equal to zero. If there is some error, it will instead return -1. 

Parameter info: https://docs.oracle.com/cd/E19620-01/805-4041/6j3r8iu2l/index.html 
return value info: https://pubs.opengroup.org/onlinepubs/009604499/functions/socket.html

5. What are the input parameters of bind() and listen()?
bind() info: https://pubs.opengroup.org/onlinepubs/009695399/functions/bind.html 
listen() info: https://vdc-download.vmware.com/vmwb-repository/dcr-public/edc96833-93a2-4837-b978-d4cc63cb3c89/48e2a331-63a8-4509-ac35-2d1b74975d3d/doc/GUID-86D86C59-67D4-454A-A80F-103E2F026C1A.html 
example: bind(int socket_fd, const struct sockaddr *address, socklen_t address_len) 
The first input parameter is the file descriptor for the socket, so it is a non-negative integer. The second parameter points to a sockaddr structure which has the address that will be bound to the socket. The third parameter has the length of this address. 

The listen() function prepares a connection-oriented server to accept client connections. The parameters of listen in the code are sockfd and 5. Sockfd is the socket descriptor for the function, while 5 is the number of requests that the system queues before it accepts the connection from the client. Increasing or decreasing the number will increase or decrease the latency. 

6.  Why use while(1)? Based on the code below, what problems might occur if there are multiple simultaneous connections to handle?

We use while(1) so that the server is constantly searching for new clients that want to connect to the server, so it just runs through that connection process repeatedly. Because we use a while loop with no way of interrupting the loop, if the server is busy handling the messages for one connection and another client tries to connect during that, it will not trigger the connection process because it is busy with the first connection. In this way it could miss a client trying to connect simultaneously. 


7. Research how the command fork() works. How can it be applied here to better handle multiple connections?
Sources: https://www.geeksforgeeks.org/fork-system-call/
https://jameshfisher.com/2017/02/25/tcp-server-fork/ 

The fork() command creates a new child process when a new process is called. So in the TCP server code, the fork() command will allow the server to connect with multiple clients. This is because fork will create a new child process for each new client that connects the server, and the new client will run under that child process, not taking away from the main process of the code. Thus multiple connections can be accepted. 

8. This program makes several system calls such as 'bind', and 'listen.' What exactly is a system call?
Info from: https://en.wikipedia.org/wiki/System_call 
A system call is just what it is called when the program has to request a service from the kernel of the OS itself for some function. 



References for client code:
.encode() and .decode() function: 
https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-handling-file-conte 

other tcp client resource:
http://pymotw.com/2/socket/tcp.html 

resource given in lab instructions for general socket info
https://realpython.com/python-sockets/#echo-client-and-server 





