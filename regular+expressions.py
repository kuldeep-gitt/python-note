import re

#search
text = "Do you know how to be a script kiddie? It's simple, just copy me."
match = re.search('script',text)
print(match.start())



#split
text = "To become a hacker%You need to think%like one."
print(re.split('%',text))
print(text.split('%'))



#findall
text = "To hack the hacker, you need to hack the hacker."
out = re.findall('hacker',text)
print(out)



#repetition pattern
#   ab*,        a with zero or more b
#   ab+,        a with one or more b
#   ab?,        a with zero or one b
#   ab{3},      a with three b's
#   ab{3,4}     a with three to four b's
text = "Do you know how to be a script kiddie? It's simple, just copy me."
out = re.findall('ow?',text)
print(out)
text = "a......ab......abb.........abbb...........aabbb"
out = re.findall('ab{2,3}',text)
print(out)



#character sets
#   [ab],       a or b
#   s[ab]+      s with one or more a or b
text = "This is a sample paragraph. Do you like paragliding?. No, I like parasailing. paraam"
out = re.findall('para[sga]+',text)
print(out)



#exclusions
#   ^           not including certain patters
text = "This is a sample exclamation! Don't overreact mate?."
out = re.findall('[^as ]+',text)
print(out)


#ranges [a-z], [A-Z], [0-9]
text = "Do you know how to be 2 a script kiddie? It's simple, just copy me."
out1 = re.findall('[0-9]+',text)
#print(out1)

out2 = re.findall('[A-Z]+',text)
#print(out2)

out3 = re.findall('[A-Z][a-z]+',text)
#print(out3)

out4 = re.findall('[A-Za-z]+',text)
print(out4)
