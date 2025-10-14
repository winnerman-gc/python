
import socket
import sys

host = '10.10.10.215'
port =9001

#connet to server using socket and port and sned get request
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
req = f'GET / HTTP/1.1\r\nHost:10.10.10.215\rnConnection: close\r\n\r\n'
s.send(req.encode())

response = b''

while True:
    data = s.recv(4096)
    if not data:
        break
    response += data

s.close()
print(response)

fileReq = f'GET /file1.txt HTTP/1.1\r\nHost:10.10.10.215\rnConnection: close\r\n\r\n'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(fileReq.encode())
response = b''
while True:
    data = s.recv(4096)
    if not data:
        break
    response += data
s.close()
print(response.decode())

fileReq = f'GET /domains HTTP/1.1\r\nHost:10.10.10.215\rnConnection: close\r\n\r\n'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(fileReq.encode())
response = b''

while True:
    data = s.recv(4096)
    if not data:
        break
    response += data
s.close()
print(response.decode())