from ast import pattern
import re

def trailing(text):
    text = input('anything') 
    pattern = re"\0+"
    location = re.search(pattern, text)