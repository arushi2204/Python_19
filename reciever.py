import socket

target_ip="127.0.0.1"
target_port=8888


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


s.bind((target_ip,target_port))

while True:
    data=s.recvfrom(100)
    print(data)

    s.sendto("NICE!".encode('ascii'),data[1])

