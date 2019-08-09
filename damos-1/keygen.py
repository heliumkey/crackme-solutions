#!/usr/bin/env python
import string
import random
import sys

def randomString(length):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(length))

#ASCII Values list
letters = []

#Generate random serial
for i in randomString(10):
    letters.append(ord(i))

#Check 4 and 5 are in range to set 0th char
if(((letters[4] + letters[5]) / 2) > 90):
    while(((letters[4] + letters[5]) / 2) > 90):
        letters[4] = ord(random.choice(string.ascii_uppercase))
        letters[5] = ord(random.choice(string.ascii_uppercase))

#Set 0th char
letters[0] = (letters[4] + letters[5]) / 2

#Set 9th char
letters[9] = letters[0] + 3

#Check 1 is in range to set 8
if((letters[1] - 0xe) < 65):
    while((letters[1] - 0xe) < 65):
        letters[1] = ord(random.choice(string.ascii_uppercase))

#Set new 8
letters[8] = letters[1] - 0xe

#Check 2 is in range to set 7
if((letters[2] + 0x14) > 90):
    while((letters[2] + 0x14) > 90):
        letters[2] = ord(random.choice(string.ascii_uppercase))

#Set new 7
letters[7] = letters[2] + 0x14

#Check 3 is in range to set 6
if((letters[3] - 6) < 65):
    while((letters[3] - 6) < 65):
        letters[3] = ord(random.choice(string.ascii_uppercase))

#Set new 6
letters[6] = letters[3] - 6

completed_serial = ""

for i in letters:
    completed_serial += chr(i)

#Print completed serial
sys.stdout.write(completed_serial + "\n")

if __name__ == "__main__":
    sys.exit()
