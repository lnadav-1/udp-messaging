import socket
import sys

# Create a UDP socket

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (str(socket.gethostbyname(socket.gethostname())), 5000)
   
    message = input("~>  ")
    encoded = message.encode()
    try:

        # Send data
        print('sending {!r}'.format(encoded))
        sent = sock.sendto(encoded, server_address)

        # Receive response
        data, server = sock.recvfrom(4096)
        #print(''.format(data))

    finally:
        
        sock.close()
