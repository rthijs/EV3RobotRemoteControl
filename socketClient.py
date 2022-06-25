import socket

HOST = "192.168.209.242"
PORT = 6666

client_socket = socket.socket()
client_socket.connect((HOST, PORT))

message = "Send me the controller data"

while True:
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(data)

client_socket.close()
