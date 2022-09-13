from ast import pattern
import re
# Task1
def reg(text1):
    pattern = r"\s"
    location = re.search(pattern, text1)
    print(location)
    print(location.span()[0])

text1 ='Berlin is a world city of culture, politics, media and science.'
reg(text1)

Task2

import re

def regX (text2):
    pattern = r"Frankfurt"
    location = re.search(pattern, text2)
    print(location)

text2 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
regX(text2)

Task3
import re
def regX (text3):
    pattern = r"\s"
    location = re.sub(pattern, '-', text3)
    print(location)

text3 = "Berlin is a city of culture."
regX(text3)

Task4

import re
def regX (text4):
    pattern = r"in"
    location = re.search(pattern, text4)
    print(location)

text4 = "Berlin is a city of culture."
regX(text4)

Task5

import re
def regX (text5):
    pattern = r"B[a-z]+"
    location = re.search(pattern, text5)
    print(location.span())
    
text5 = "Berlin is a city of culture."
regX(text5)

Task6
import re
def regX (text6):
    pattern = r"ai"
    location = re.findall(pattern, text6)
    print(len(location))
    
text6 = "The rain in Spain."
regX(text6)
