#1. What is the most frequent word in the following paragraph?
import re

paragraph = '''I love teaching. If you do not love teaching
what else can you love. I love Python if you do not love
something which can give you all the capabilities to develop
an application what else can you love.'''

words = re.findall(r'\b\w+\b',paragraph)
worddic = {}
for word in words:
    if word in worddic:
        worddic[word] +=1
    else:
        worddic[word] = 1

result = [(count,word) for word, count in worddic.items()]
result.sort(reverse=True)
print(result)

'''2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in
the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract
these numbers from this whole text and find the distance between the two
furthest particles.'''
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
intpoint = [int(x) for x in points]
print(intpoint)
print("dist =",max(intpoint)-min(intpoint))

#level 2 
'''1. Write a pattern which identifies if a string is a valid python variable'''

def is_valid_variable(vari):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, vari))

print(is_valid_variable("hjkshf"))

#level 3
#1. Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve
%tea@ching%;. There $is nothing; &as& mo@re rewarding as
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s
mo@tivate yo@u to be a tea@cher!?'''

def clean_text(sent):
    return re.sub('[%,@#;!?$]',"",sent)
print(clean_text(sentence))

from collections import Counter

def most_frequent_words(text):
    words = text.split()
    freq = Counter(words)
    return freq.most_common(3)

print(most_frequent_words(sentence))

