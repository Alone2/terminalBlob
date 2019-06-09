#!/usr/bin/python3
import random

print("Content-type: text/html\n")

RED = '\033[0;31m'
NOCOLOR = '\033[0m' 
GREEN = '\33[0;21m'
YELLOW = '\33[0;33m'
BLUE = '\33[0;34m'
CYAN =  '\33[0;36m'

ALL = [RED,NOCOLOR,GREEN,YELLOW,BLUE,CYAN]

r = open("pics/blobber.txt", "r")
txt = r.read()
r.close()

print(random.choice(ALL) + txt)
