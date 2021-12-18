"""
helicopter.py - Anurag M
MIT License
A simple script to print a helicopter animation to the terminal.
All the files has to be in the same folder.
Usage
=====
To run normally use
    python heli.py
"""

import os
import time
import random

left = True
while True:
   os.system("cat h.txt")
   if left:
       os.system("cat l.txt")
   else:
       os.system("cat r.txt")
   time.sleep(0.2)
   left = not left
   os.system('clear')
