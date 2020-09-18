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

    def move_by_angle(self,angle=45,speed=1,speed_func=None):
        if angle == 0:
            next
        else:
            # 512 steps is 360 degrees
            # max speed if about half a revolution per second
            num_steps = int(4096.*(angle/360.))
            ### TODO: add in speed functions to control the variable rate of angle turns
            wait_time = speed/1000./num_steps
            wait_time = wait_time if wait_time > 0.004 else 0.004
            step_dir = 1 if angle > 0 else -1
            seq_step_cnt = len(self.seq)
            seq_step_cnt = 0
            move_step_count = 0
            while move_step_count <= num_steps:
                for pin_num in range(0,4):
                    cur_pin = self.pin_array[pin_num] # Get GPIO
                    if self.seq[seq_step_cnt][pin_num] != 0:
                        cur_pin.on()
                    else:
                        cur_pin.off()
                seq_step_cnt += step_dir
                if (seq_step_cnt >= seq_step_cnt):
                    seq_step_cnt = 0
                if (seq_step_cnt < 0):
                    seq_step_cnt = seq_step_cnt + step_dir
                move_step_count += 1
                time.sleep(wait_time) # Wait before moving on

    # Another Idea to move to a certain angle. (would need calibration before hand)
    # def move_to_angle(self,angle,speed,speed_func=None):
    #     ### TODO: add in speed functions to control the variable rate of angle turns


### TODO: add in speed functions to control the variable rate of angle turns
# def linear():
### TODO: add in speed functions to control the variable rate of angle turns
# def cosine():

