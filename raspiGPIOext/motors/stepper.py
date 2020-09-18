import time
import sys
from gpiozero import OutputDevice as stepper


class Stepper_ROHS_28BYJ48():

    def __init__(self,pin_array):
        # moves by angle in degrees
        # angle: degrees +/- [default: +45]
        # speed: milliseconds [default: 1000ms]
        # speed_func: string - ex: 'linear', 'cosine', etc... [default: 'linear']
        self.pin_array = [stepper(pin) for pin in pin_array]
        self.seq = [[1,0,0,1],
                    [1,0,0,0], 
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1]]

    def move_by_angle(self,angle=45,speed=1000,speed_func=None):
        if angle == 0:
            next
        else:
            ### TODO: add in speed functions to control the variable rate of angle turns
            wait_time = speed/float(1000) if speed/float(1000) > 0.004 else 0.004
            step_dir = 1 if angle > 0 else -1
            step_count = len(seq)
            step_counter = 0
            while True: # Start main loop
                for pin_num in range(0,4):
                    cur_pin = self.pin_array[pin_num] # Get GPIO
                    if seq[step_counter][pin_num]!=0:
                        cur_pin.on()
                    else:
                        cur_pin.off()
                step_counter += step_dir
                if (step_counter >= step_count):
                    step_counter = 0
                if (step_counter < 0):
                    step_counter = step_count + step_dir
                time.sleep(wait_time) # Wait before moving on

    # Another Idea to move to a certain angle. (would need calibration before hand)
    # def move_to_angle(self,angle,speed,speed_func=None):
    #     ### TODO: add in speed functions to control the variable rate of angle turns


### TODO: add in speed functions to control the variable rate of angle turns
# def linear():
### TODO: add in speed functions to control the variable rate of angle turns
# def cosine():

