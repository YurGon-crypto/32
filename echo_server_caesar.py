import socket


def caesar_cipher(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - offset + key) % 26 + offset)
        else:
            result += char
    return result


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 5555)
server_socket.bind(server_address)

print('UDP Echo Server with Caesar Cipher is listening on {}:{}'.format(*server_address))

while True:

    data, client_address = server_socket.recvfrom(1024)

    key = int(data.decode())
    response_message = caesar_cipher(data.decode(), key)

    server_socket.sendto(response_message.encode(), client_address)
