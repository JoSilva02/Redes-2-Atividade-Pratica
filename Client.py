import socket

# Sistema de Upload/Download de Arquivos
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
client_socket.send(b'Hello World')
client_socket.close()