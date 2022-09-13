from ast import pattern
import re

def reg(text1):
    pattern = r"\s"
    location = re.search(pattern, text1)
    print(location)
    print(location.span()[0])

text1 ='Berlin is a world city of culture, politics, media and science.'
reg(text1)