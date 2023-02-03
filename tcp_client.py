"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():
    #designating IP address and port number
    hostname = "172.20.10.3"
    portnum = 10000
    # Creates a socket and connects it to the server at the designated IP and port
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.connect((hostname, portnum))
    
    # Gets user input and sends it to the server using our TCP socket
    usrinput = input("Enter an input: ")
    #use .encode() to convert to the string to bytes in order to be read by server
    tcp_sock.sendall(usrinput.encode())
    
    # Receives a response from the server and closes the TCP connection
    msg = tcp_sock.recv(256)
    #decoded message from bytes to string to get rid of "b" at beginning of message
    print(msg.decode())
    tcp_sock.close()
    pass


if __name__ == '__main__':
    main()
