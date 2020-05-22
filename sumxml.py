#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = input("Enter location: ")
print ("Retrieving " + url)

file = urlopen(url)
xml = file.read()
print ("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print ("Count: " + str(len(counts)))

accumulator = 0

for count in counts:
    accumulator += int(count.text)

print ("Sum:" + str(accumulator))
