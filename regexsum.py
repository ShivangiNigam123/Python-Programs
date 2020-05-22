#read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re

name = input ("enter file :")
sum = 0
fhandle = open(name)
numlist = list()
for line in fhandle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+',line)
    for number in numbers :
        sum = sum + int(number)

print(sum)
