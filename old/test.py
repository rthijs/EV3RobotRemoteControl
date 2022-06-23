#!/usr/bin/env python3

from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, LargeMotor, MoveTank, SpeedPercent)

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 10)