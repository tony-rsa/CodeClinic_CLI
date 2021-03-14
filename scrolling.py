import blessings
import os

term = blessings.Terminal()
with term.fullscreen():
    while True:
        term.move(0, 0) # move to top of screen
        print('fish simulation')
        term.sleep(1)