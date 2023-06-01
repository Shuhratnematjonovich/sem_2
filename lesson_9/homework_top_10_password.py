""" How To Find Most Frequent Word In Text File """

import re 
from collections import Counter

with open("pwd.txt", 'r') as passw:
    with open("news.txt", 'w') as f:
        for i in passw:
            x = i.partition(";")
            f.write(f'{x[2]}')

with open("news.txt", encoding='utf-8') as file:
    all_words = re.findall(r"[0-9a-zA-Z-']+",file.read())
    all_words = [word.upper() for word in all_words]

    
word_counts = Counter()
for word in all_words:
    word_counts[word]+=1

with open('password.txt', mode='w') as pword:
    pword.write(' Top 10 passwords\n')
    for word in word_counts.most_common(10):
        pword.write(f'\n{word[0],word[1]}')
