"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():

    hostname = "172.20.10.3"
    portnum = 10000
    # TODO: Create a socket and connect it to the server at the designated IP and port
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.connect((hostname, portnum))
    
    # TODO: Get user input and send it to the server using your TCP socket
    usrinput = input("Enter an input: ")
    tcp_sock.sendall(usrinput.encode())
    
    # TODO: Receive a response from the server and close the TCP connection
    msg = tcp_sock.recv(256)
    #decoded message to get rid of "b" at beginning of message
    print(msg.decode())
    tcp_sock.close()
    pass


if __name__ == '__main__':
    main()
