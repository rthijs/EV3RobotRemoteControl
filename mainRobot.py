#!/usr/bin/env python3

import os
from time import sleep
from robot import Robot

robot = Robot()

robot.set_left_motor_speed(100)
sleep(1)
robot.set_left_motor_speed(0)
robot.set_right_motor_speed(100)
sleep(1)
robot.set_right_motor_speed(0)

os._exit(0)