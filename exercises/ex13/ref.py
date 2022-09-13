import re  # import the regular expression library

text_to_be_searched = "some text mail@web.de some text i,Am,feeling,Good!"  # target text

pattern = r"[a-z],[A-Z]"  # the actual regular expression (r stands for raw string)

#x = re.search(pattern, text_to_be_searched)  # using the pattern to search the target text
x = re.findall(pattern, text_to_be_searched)

print(x)  # printing out the match