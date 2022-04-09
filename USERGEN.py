#!/usr/bin/env python3

import random
import string

with open('cirt-default-usernames.txt', 'r') as infile:
    nouns = infile.read().strip(' \n').split('\n')
with open('names1.txt', 'r') as infile:
    adjectives = infile.read().strip(' \n').split('\n')
with open('top-usernames-shortlist.txt','r') as inline:
    censored = inline.read().strip(' \n').split('\n')
for count in range(1, 51):
    word1 = random.choice(adjectives)
    word2 = random.choice(nouns)
    word1 =word1.title()
    word2 =word2.title()
    username = '{}{}'.format(word1, word2)

    print("username" + str(count) + " = " + username)
