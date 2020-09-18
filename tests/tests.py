from raspiGPIOext.motors.stepper import Stepper_ROHS_28BYJ48

stepper_motor = Stepper_ROHS_28BYJ48([7,11,13,15])

stepper_motor.move_by_angle(angle=45,speed=1)
stepper_motor.move_by_angle(angle=90,speed=.5)
stepper_motor.move_by_angle(angle=-45,speed=.5)