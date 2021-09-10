import json
import socket
sock = socket.socket()
sock.bind(("0.0.0.0",2222))
#sock.bind(('localhost',9999))

sock.listen(5)

while True:
    fd, address = sock.accept()
    print(address)
    while True:
        if not fd:
            break
        received_size = 0
        data = fd.recv(1024)
        fd.send(b'1')
        total_size = json.loads(data.decode('utf-8'))['filesize']
        file_name = json.loads(data.decode('utf-8'))['filename']
        f = open(file_name,"wb")
        while int(received_size) < int(total_size):
            data = fd.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print("send done")
            fd.close()