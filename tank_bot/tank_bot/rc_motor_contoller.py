# import curses and GPIO
import curses
import RPi.GPIO as GPIO
import os  # added so we can shut down OK
import time  # import time module
from evdev import InputDevice


# GPIO.cleanup()
#
# # set GPIO numbering mode and define output pins
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7, GPIO.OUT)
# GPIO.setup(11, GPIO.OUT)
# GPIO.setup(13, GPIO.OUT)
# GPIO.setup(15, GPIO.OUT)
# # GPIO.setup(29, GPIO.OUT)
#
# # for x in range(1, 10):
# #     GPIO.output(29, False)
# #     time.sleep(.5)
# #     GPIO.output(29, True)
# #     time.sleep(1)
#
# # Get the curses window, turn off echoing of keyboard to screen, turn on
# # instant (no waiting) key response, and use special values for cursor keys
# screen = curses.initscr()
# curses.noecho()
# curses.cbreak()
# screen.keypad()
#
# try:
#     while True:
#         char = screen.getch()
#         if char == ord('q'):
#             break
#         if char == ord('S'):  # Added for shutdown on capital S
#             os.system('sudo shutdown now')  # shutdown right now!
#         elif char == curses.KEY_UP:
#             GPIO.output(7, False)
#             GPIO.output(11, True)
#             GPIO.output(13, False)
#             GPIO.output(15, True)
#         elif char == curses.KEY_DOWN:
#             GPIO.output(7, True)
#             GPIO.output(11, False)
#             GPIO.output(13, True)
#             GPIO.output(15, False)
#         elif char == curses.KEY_RIGHT:
#             GPIO.output(7, True)
#             GPIO.output(11, False)
#             GPIO.output(13, False)
#             GPIO.output(15, True)
#         elif char == curses.KEY_LEFT:
#             GPIO.output(7, False)
#             GPIO.output(11, True)
#             GPIO.output(13, True)
#             GPIO.output(15, False)
#         elif char == 10:
#             GPIO.output(7, False)
#             GPIO.output(11, False)
#             GPIO.output(13, False)
#             GPIO.output(15, False)
#
# finally:
#     # Close down curses properly, inc turn echo back on!
#     curses.nocbreak()
#     screen.keypad(0)
#     curses.echo()
#     curses.endwin()
#     GPIO.cleanup()

import RPi.GPIO as GPIO
import os #added so we can shut down OK
import time #import time module
from evdev import InputDevice, categorize, ecodes

GPIO.cleanup()

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
# GPIO.setup(29, GPIO.OUT)
#
# for x in range(1, 10):
#         GPIO.output(29,False)
#         time.sleep(.5)
#         GPIO.output(29,True)
#         time.sleep(1)


device = InputDevice("/dev/input/event0") # my keyboard
device_status = True
try:
    while device_status:
        for event in device.read_loop():
            if event.type == ecodes.EV_KEY:
                key = str(categorize(event)).split("(")[1].split(")")[0]
                key_press = str(categorize(event)).split("), ")[1]
                if key == 'KEY_Q':
                    device_status = False
                elif key == "KEY_UP":
                    GPIO.output(7, False)
                    GPIO.output(11, True)
                    GPIO.output(13, False)
                    GPIO.output(15, True)
                elif key == "KEY_DOWN":
                    GPIO.output(7, True)
                    GPIO.output(11, False)
                    GPIO.output(13, True)
                    GPIO.output(15, False)
                elif key == "KEY_RIGHT":
                    GPIO.output(7, True)
                    GPIO.output(11, False)
                    GPIO.output(13, False)
                    GPIO.output(15, True)
                elif key == "KEY_LEFT":
                    GPIO.output(7, False)
                    GPIO.output(11, True)
                    GPIO.output(13, True)
                    GPIO.output(15, False)
                elif key == "KEY_ENTER":
                    GPIO.output(7, False)
                    GPIO.output(11, False)
                    GPIO.output(13, False)
                    GPIO.output(15, False)

finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    GPIO.cleanup()

