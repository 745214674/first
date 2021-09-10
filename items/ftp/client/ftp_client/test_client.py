import json
import os.path
import socket
import sys

socket = socket.socket()
socket.connect(('172.26.1.2',2222))
#socket.connect(('localhost',9999))
while True:
    cmd = input(':>').strip()
    if len(cmd) ==0:continue
    file_size = os.path.getsize(cmd)
    data = {
        'filesize':file_size,
        "filename":cmd
    }

    socket.send(json.dumps(data).encode())
    socket.recv(1024)
    f = open(cmd, 'rb')
    for line in f:
        socket.send(line)

    else:
        print("send done")
        f.close()

