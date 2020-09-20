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
        
        # minimum functional time between steps:
        self.min_wait = 0.00075
        # 4096 steps is 360 degrees
        self.steps_360 = 4096
        # sequence array
        self.seq = [[1,0,0,1],
                    [1,0,0,0], 
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1]]
        
        

    def move_by_angle(self,angle=45,speed=1,speed_func=None):
        # print('\n\nStarting with angle:',angle,'and duration:',speed,'seconds')
        if angle == 0:
            next
        else:
            num_steps = abs(int(self.steps_360*(angle/360.)))
            ### TODO: add in speed functions to control the variable rate of angle turns
            wait_time = speed/num_steps
            wait_time = wait_time if wait_time > self.min_wait else self.min_wait
            step_dir = 1 if angle > 0 else -1
            seq_step_cnt = 0
            move_step_count = 0
            while move_step_count <= abs(num_steps):
                start_time = time.time()
                for pin_num in range(0,4):
                    cur_pin = self.pin_array[pin_num]
                    if self.seq[seq_step_cnt][pin_num] != 0:
                        cur_pin.on()
                    else:
                        cur_pin.off()
                if (abs(seq_step_cnt) >= (len(self.seq)-1)):
                    seq_step_cnt = 0
                else:
                    seq_step_cnt = seq_step_cnt + step_dir
                move_step_count += 1
                time.sleep(wait_time-(time.time()-start_time)) # Wait before moving on

    # Another Idea to move to a certain angle. (would need calibration before hand)
    # def move_to_angle(self,angle,speed,speed_func=None):
    #     ### TODO: add in speed functions to control the variable rate of angle turns


### TODO: add in speed functions to control the variable rate of angle turns
# def linear():
### TODO: add in speed functions to control the variable rate of angle turns
# def cosine():