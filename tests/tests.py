from raspiGPIOext.motors.stepper import Stepper_ROHS_28BYJ48

stepper_motor = Stepper_ROHS_28BYJ48([12,16,20,21])

#stepper_motor.move_by_angle(angle=360,speed=3.5)
stepper_motor.move_by_angle(angle=90,speed=.5)
#stepper_motor.move_by_angle(angle=-45,speed=.5)
