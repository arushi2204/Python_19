import socket

target_ip="127.0.0.1"
target_port=8888


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data=input("Enter your message --->>>   ")
    msg=data.encode('ascii')
    s.sendto(msg,(target_ip,target_port))
    print(s.recvfrom(100))

