import re
from functools import reduce

ss = open("input.txt").readlines()
    
p1 = sum([int(re.findall(r'\d', s)[0]+re.findall(r'\d', s)[-1]) for s in ss])
print(p1)

d = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}
ss = [reduce(lambda s, kv: s.replace(*kv), d.items(), s) for s in ss]
p2 = sum([int(re.findall(r'\d', s)[0]+re.findall(r'\d', s)[-1]) for s in ss])
print(p2)