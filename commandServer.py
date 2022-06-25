#!/usr/bin/env python3

import socket
import json
from inputs import get_gamepad

def run_server():
    HOST = "192.168.209.242" #socket.gethostname()
    PORT = 6666

    EVENTS_TO_SEND = ("ABS_Y", "ABS_RY")

    print("Hosting server on " + HOST + ":" + str(PORT))

    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)

    conn, addr = server_socket.accept()
    print("Connection from: " + str(addr))
    
    #run server forever
    while True:
        data = conn.recv(1024).decode()

        data_dict = {}

        events = get_gamepad()
        for event in events:
            ev_type = event.ev_type
            ev_code = event.code
            ev_state = event.state
            if (ev_type=='Absolute' and ev_code in EVENTS_TO_SEND):
                data_dict = {
                    "code": ev_code,
                    "state": ev_state
                }

        data_json = json.dumps(data_dict)
        #if (data_json != {}):
        #    print(data_json)
        conn.send(data_json.encode())
        
    conn.close()

if __name__ == '__main__':
    run_server()