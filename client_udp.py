import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_address = ('localhost', 5555)


message = 'Hello, server!'


client_socket.sendto(message.encode(), server_address)


response, server_address = client_socket.recvfrom(1024)

print('Received response from server:', response.decode())

client_socket.close()
