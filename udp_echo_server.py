import socket
import sys

# list of people
users = []
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = (str(socket.gethostbyname(socket.gethostname())), 5000)
#server_address = ('localhost', 5000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
print("Ready")
while True:
    data, address = sock.recvfrom(4096)
    users.append(address)
    #print('received {} bytes from {}'.format(len(data), address))
    print(address[0]," ",data.decode())

    if data:
        sent = sock.sendto("Recived!".encode(), address)
        #print('sent {} bytes back to {}'.format(sent, address))
