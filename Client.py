import socket
import sys
import threading


def code():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 9999)

    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:
        # Send data
        message = b'ThisIsAnUsername'
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(1024)
            amount_received += len(data)
            msg = '{!r}'.format(data)
            print("receive: "+msg[1:])
            break
    finally:
        print('closing socket')
        sock.close()


for i in range(1):
    hilo1 = threading.Thread(target=code)
    hilo1.start()
