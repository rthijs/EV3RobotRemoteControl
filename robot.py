#!/usr/bin/env python3
from time import sleep
from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, LargeMotor)

class Robot():

    def __init__(self):
        print("Initializing robot...")
        self._motor_left = LargeMotor(OUTPUT_A)
        self._motor_right = LargeMotor(OUTPUT_B)
        self._motor_left_speed = 0
        self._motor_right_speed = 0

    def update_robot(self):
        while True:
            self._motor_left.on(self._motor_left_speed)
            self._motor_right.on(self._motor_right_speed)
            #print("motor speeds: " + str(self._motor_left_speed) + ":" + str(self._motor_right_speed))
            sleep(0.02)

    def set_left_motor_speed(self, speed):
        #print("Setting left motor speed to: " + str(speed))
        self._motor_left_speed = speed

    def set_right_motor_speed(self, speed):
        #print("Setting right motor speed to: " + str(speed))
        self._motor_right_speed = speed

if __name__ == "__main__":
    pass