from djitellopy import Tello
from time import sleep

tello = Tello()
tello.connect()
print(tello.get_battery())

# movements are in centimeters sleep is in seconds
# send_rc_control(right/left, forward/backward, up/down, rotate clockwise/counter clockwise)
# units put in -100-100 are % of speed. negative numbers are left/ backwards/ down/ counter clockwise

tello.takeoff()
sleep(1)
tello.send_rc_control(0, 0, 50, 0)
sleep(3.5)
tello.send_rc_control(0, 50, 0, 0)
sleep(2.7)
tello.send_rc_control(-50, 0, 0, 0)
sleep(2.7)
tello.send_rc_control(0, -50, 0, 0)
sleep(2.7)
tello.send_rc_control(50, 0, 0, 0)
sleep(2.7)
tello.send_rc_control(0, 0, 0, 0)
tello.flip_forward()
sleep(1)
tello.land()
tello.end()
