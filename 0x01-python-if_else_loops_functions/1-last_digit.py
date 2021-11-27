#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
note = "Last digit of {:d} is {:d} and is"
if number < 0 and lastDigit != 0:
    lastDigit = -(10 - lastDigit)
if lastDigit > 5:
    print("{:s} greater than 5".format(note).format(number, lastDigit))
elif lastDigit < 6 and lastDigit != 0:
    print("{:s} less than 6 and not 0".format(note).format(number, lastDigit))
elif lastDigit == 0:
    print("{:s} 0".format(note).format(number, lastDigit))
