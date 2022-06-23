from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent)

class Robot():    

    tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
    tank_drive.on(0,0)

    def __init__(self):
        print("Initializing robot...")
        self.motor_left_speed = 0
        self.motor_right_speed = 0

    def drive(self,speed):
        print("driving with speed: " + str(speed))
        self.tank_drive.on(SpeedPercent(100), SpeedPercent(100))

if __name__ == '__main__':
    pass 