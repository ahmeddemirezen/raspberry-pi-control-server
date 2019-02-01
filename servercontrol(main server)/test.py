import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="192.168.1.198"
port=9898
buf=1024

print type(host),type(port)

s.bind((host,port))
s.listen(1)
addr,ip=s.accept()
while True:
    addr.send(raw_input("gonderilecek komut"))
