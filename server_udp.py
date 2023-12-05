import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_address = ('localhost', 5555)
server_socket.bind(server_address)

print('UDP Server is listening on {}:{}'.format(*server_address))

while True:

    data, client_address = server_socket.recvfrom(1024)

    print('Received data from {}: {}'.format(client_address, data.decode()))

    response_message = 'Hello, client! Your message was received.'
    server_socket.sendto(response_message.encode(), client_address)
