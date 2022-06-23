#!/usr/bin/env python3

from time import sleep
from old.robot import Robot

robot = Robot()

robot.drive(50)
sleep(1)
robot.drive(100)
sleep(1)
robot.drive(0)