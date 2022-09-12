#!/usr/bin/env python3

import random
import string

with open('names.txt', 'r') as infile:
    list1 = infile.read().strip(' \n').split('\n')
with open('names1.txt', 'r') as infile:
    list2 = infile.read().strip(' \n').split('\n')
#with open('top-usernames.txt','r') as inline:
#    censored = inline.read().strip(' \n').split('\n')
for count in range(1, 51):
    word1 = random.choice(list1)
    word2 = random.choice(list2)
    word1 = word1.title()
    word2 = word2.title()
    username = '{}{}'.format(word1, word2)

    print("username" + str(count) + " = " + username)
