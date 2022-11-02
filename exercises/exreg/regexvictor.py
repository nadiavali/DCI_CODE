import re



text = """Hey Mr. Bezos,

I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions! 

therealjeffabcbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pacaintdeadandnowchillinonwrongislands@mail.com
999.445.090
334-999-878
567 888 999
Kind regards,
Tanisha"""
text1 ='janHey!'
meta_characters = ''' . ^ $ * + ? { } [ inside this you dont need to be escaped] \ | ( )  (need to be escaped) '''
# with \ you can scape the effect of them
pattern = re.compile(r'\d{3}.\d{3}.\d{3}') #[1-5] range between 1 to 5 #[89] 8 or 9
#[a-zA-Z] #all lower and upper letters
#pattern = re.compile(r'[^Hey]') 
# ^Hey means start with Hey
# [^Hey] means every thing but not Hey


matches = pattern.finditer(text)

for match in matches:
    print(match)
"<re.Match object; span=(331, 334), match='abc'>"  # span is where the match got found

# parsing data from text with regex

# with open('regex.txt','r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)


