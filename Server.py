import socket

# TCP Server -- Colab Slide/Google Site
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.bind(5)
print("Starting the server at localhost: 12345")
while True:
    client_server, address = server_socket.accept()
    data = client_server.recv(1024)
    print(f"Received from {address}: {data.decode()}")
    client_server.close()