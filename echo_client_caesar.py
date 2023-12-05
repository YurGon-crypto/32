import socket


def caesar_cipher(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - offset - key) % 26 + offset)
        else:
            result += char
    return result


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 5555)


key = 3
message = 'Hello, server!'


client_socket.sendto(str(key).encode(), server_address)


client_socket.sendto(message.encode(), server_address)


response, server_address = client_socket.recvfrom(1024)


decrypted_response = caesar_cipher(response.decode(), key)
print('Received decrypted response from server:', decrypted_response)


client_socket.close()
