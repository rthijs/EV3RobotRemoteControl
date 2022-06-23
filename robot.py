#!/usr/bin/env python3

from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, LargeMotor)

class Robot():

    def __init__(self):
        print("Initializing robot...")
        self._motor_left = LargeMotor(OUTPUT_A)
        self._motor_right = LargeMotor(OUTPUT_B)
        self._motor_left_speed = 0
        self._motor_right_speed = 0

    def update_robot(self):
        self._motor_left.on(self._motor_left_speed)
        self._motor_right.on(self._motor_right_speed)

    def set_left_motor_speed(self, speed):
        self._motor_left_speed = speed
        self.update_robot()

    def set_right_motor_speed(self, speed):
        self._motor_right_speed = speed
        self.update_robot()

if __name__ == "__main__":
    pass