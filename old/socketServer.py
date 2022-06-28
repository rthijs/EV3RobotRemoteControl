#!/usr/bin/env python3

import socket
import selectors
import types

HOST = "127.0.0.1"
PORT = 1983

selector = selectors.DefaultSelector()

listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening_socket.bind((HOST, PORT))
listening_socket.listen()
print(f"Listening on {(HOST, PORT)}")
listening_socket.setblocking(False)

selector.register(listening_socket, selectors.EVENT_READ, data=None)

def accept_wrapper(socket):
    connection, address = socket.accept()
    print(f"Accepted connection from {address}")
    connection.setblocking(False)
    data = types.SimpleNamespace(addr=address, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    selector.register(connection, events, data=data)

def service_connection(key, mask):
    socket = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = socket.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            print(f"Closing connection to {data.addr}")
            selector.unregister(socket)
            socket.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {data.outb!r} to {data.addr}")
            sent = socket.send(data.outb)
            data.outb = data.outb[sent:]

try:
    while True:
        events = selector.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    selector.close()

