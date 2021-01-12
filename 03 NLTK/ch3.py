# Aaliya Hussain
# 2nd Period

import nltk, re, pprint
from nltk import word_tokenize
from urllib import request

# Exercise 20
from urllib.request import urlopen
from bs4 import BeautifulSoup
#
# url = "https://stackoverflow.com/questions"
# webpage = urlopen(url).read().decode("utf8")
# raw = BeautifulSoup(webpage, "html.parser")
# questions = raw.find(id="questions")
# top = questions.find(class_="summary")
# text = top.text.split("\n")
# print(text[1])

# Exercise 22
# url = "http://news.bbc.co.uk/"
# webpage = urlopen(url).read().decode("utf8")
# raw = BeautifulSoup(webpage, "html.parser").get_text()
# try1 = re.findall("[A-Z][a-z]*", raw)
# try2 = re.findall("\w+|\S\w*", raw)
# try3 = re.findall("\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw)
# try4 = re.findall('''(?x)(?:[A-Z]\.)+| \w+(?:-\w+)*| \$?\d+(?:\.\d+)?%?| \.\.\.| [][.,;"'?():-_`]''', raw)
# print(" ".join(try1))
# print(" ".join(try2))
# print(" ".join(try3))
# print(" ".join(try4))

# Soundex
# def soundex(w):
#     word = w.lower()
#     code = word[0]
#     word_list = list(word)
#     consonants = {"b":1, "f": 1, "p":1, "v":1, "c":2, "g":2, "j":2, "k":2, "q":2, "s":2, "x":2, "z":2, "d":3, "t":3, "l":4, "m":5, "n":5, "r":6}
#     for let in range(1, len(word)):
#         if word_list[let] in consonants:
#             word_list[let] = str(consonants[word_list[let]])
#     for let in range(1, len(word)):
#         if len(code) == 4:
#             break
#         if let == 1 and word[0] in consonants and str(consonants[word[0]]) == word_list[let]:
#             continue
#         if let > 1:
#             if word_list[let] == word_list[let-1]:
#                 continue
#         if let > 2:
#             if word_list[let] == word_list[let-2] and (word_list[let-1] == "h" or word_list[let-1] == "w"):
#                 continue
#         if word_list[let].isdigit():
#             code += word_list[let]
#     if len(code) < 4:
#         code += "0"
#     return code.upper()
#
# print(soundex("Pfister"))

# List Comprehensions
words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
vsequences = {"".join(ch for ch in word if ch in "aeiou") for word in words}
print(sorted(vsequences))