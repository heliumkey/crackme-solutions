#!/usr/bin/env python
import string
import random
import sys

def randomString(length):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(length))

#Letters list
letters = []
#ASCII Values list
letterV = []

#Generate random serial
for i in randomString(10):
    letters.append(i)
    letterV.append(ord(i))

#Check 4 and 5 are in range to set 0th char
if(((letterV[4] + letterV[5]) / 2) > 90):
    while(((letterV[4] + letterV[5]) / 2) > 90):
        letterV[4] = ord(random.choice(string.ascii_uppercase))
        letterV[5] = ord(random.choice(string.ascii_uppercase))

#Set 0th char in both arrays
letters[0] = chr((letterV[4] + letterV[5]) / 2)
letterV[0] = (letterV[4] + letterV[5]) / 2

#Set 9th char in both arrays
letters[9] = chr(letterV[0] + 3)
letterV[9] = letterV[0] + 3

#Check 1 is in range to set 8
if((letterV[1] - 0xe) < 65):
    while((letterV[1] - 0xe) < 65):
        letterV[1] = ord(random.choice(string.ascii_uppercase))

#Set new 1 or do nothing if unchanged        
letters[1] = chr(letterV[1])

#Set new 8
letterV[8] = letterV[1] - 0xe
letters[8] = chr(letterV[8])

#Check 2 is in range to set 7
if((letterV[2] + 0x14) > 90):
    while((letterV[2] + 0x14) > 90):
        letterV[2] = ord(random.choice(string.ascii_uppercase))
#Set new 2 or do nothing
letters[2] = chr(letterV[2])

#Set new 7
letterV[7] = letterV[2] + 0x14
letters[7] = chr(letterV[7])

#Check 3 is in range to set 6
if((letterV[3] - 6) < 65):
    while((letterV[3] - 6) < 65):
        letterV[3] = ord(random.choice(string.ascii_uppercase))

#Set new 3 or do nothing
letters[3] = chr(letterV[3])

#Set new 6
letterV[6] = letterV[3] - 6
letters[6] = chr(letterV[6])

completed_serial = ""

for i in letterV:
    completed_serial += chr(i)

#Print completed serial
sys.stdout.write(completed_serial + "\n")

if __name__ == "__main__":
    sys.exit()
