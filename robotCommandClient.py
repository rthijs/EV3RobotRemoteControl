#!/usr/bin/env python3
import threading
import socket
import json
from robot import Robot

def normalize_speed(value):
    if (value < 9000 and value > -9000):
        return 0
    else:
        return value / 32768 * 100 * -1


class RobotCommandClient():

    ev3 = Robot()

    update_thread = threading.Thread(target=ev3.update_robot)
    update_thread.start()


    HOST = "192.168.209.242"
    PORT = 6666

    client_socket = socket.socket()
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.connect((HOST, PORT))

    message = "ready"

    while True:
        client_socket.send(message.encode())
        data_json = client_socket.recv(1024).decode()
        # print(data_json)
        data = json.loads(data_json)
        if (data != {}):
            normalized_speed = normalize_speed(data["state"])
            if data["code"]  == "ABS_Y":
                ev3.set_left_motor_speed(normalized_speed)
            if data["code"] == "ABS_RY":
                ev3.set_right_motor_speed(normalized_speed)

