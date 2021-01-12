# Aaliya Hussain
# 2nd Period

import nltk

# Exercise 4
# from nltk.corpus import inaugural
# graph = nltk.ConditionalFreqDist((target, fileid[:4]) for fileid in inaugural.fileids() for w in inaugural.words(fileid) for target in ["men", "women", "people"] if w.lower() == target)
# graph.plot()

# Exercise 5
# from nltk.corpus import wordnet as wn
# word = [ss.name() for ss in wn.synsets("water")]
# print(word)
# word_pm = [ss.lemma_names() for ss in wn.synset(word[5]).part_meronyms()]
# print(word_pm)
# word_sm = [ss.lemma_names() for ss in wn.synset(word[5]).substance_meronyms()]
# print(word_sm)
# word_mm = [ss.lemma_names() for ss in wn.synset(word[5]).member_meronyms()]
# print(word_mm)
# word_mh = [ss.lemma_names() for ss in wn.synset(word[5]).member_holonyms()]
# print(word_mh)
# word_ph = [ss.lemma_names() for ss in wn.synset(word[5]).part_holonyms()]
# print(word_ph)
# word_sh = [ss.lemma_names() for ss in wn.synset(word[5]).substance_holonyms()]
# print(word_sh)

# Exercise 7
# from nltk.corpus import gutenberg
#
# for f in gutenberg.fileids():
#     text = nltk.Text(gutenberg.words(f))
#     cons = text.concordance_list("however", lines=200)
#     b = 0
#     p = 0
#     o = 0
#     for c in cons:
#         check = c.line
#         if ", however ," in check or ", however ." in check or ", however ;" in check:
#             p += 1
#         elif ". However" in check or "; however" in check:
#             b += 1
#         elif "however" in check or "However" in check:
#             o += 1
#     print(f)
#     print("Beginning: %s" % b)
#     print("Parenthetical: %s" % p)
#     print("Other: %s" % o)
#     print()

# Exercise 9
# from nltk.corpus import gutenberg
# paradise = nltk.Text(gutenberg.words("milton-paradise.txt"))
# alice = nltk.Text(gutenberg.words("carroll-alice.txt"))
#
# print("paradise")
# paradise.concordance("just")
# print()
# print("alice")
# alice.concordance("just")

# Exercise 12
# d = nltk.corpus.cmudict.entries()
# distinct = set()
# rpts = 0
# for e in d:
#     if e[0] in distinct:
#         rpts += 1
#     distinct.add(e[0])
# print(len(distinct))
# print(rpts)
# print(rpts/len(distinct))

# Exercise 17
# def fifty_common(text):
#     from nltk.corpus import stopwords
#     import re
#     stop_w = set(stopwords.words("english"))
#     non_stop = nltk.FreqDist(w.lower() for w in text if w.lower() not in stop_w and re.search("[a-z]", w.lower()))
#     return non_stop.most_common(50)
#
# from nltk.corpus import gutenberg
# print(fifty_common(gutenberg.words("carroll-alice.txt")))

# Exercise 18
# def fifty_bigrams(text):
#     from nltk.corpus import stopwords
#     import re
#     stop_w = set(stopwords.words("english"))
#     bigrams = nltk.bigrams(text)
#     ret = nltk.FreqDist(w for w in bigrams if w[0].lower() not in stop_w and re.search("[a-z]", w[0].lower()) and w[1].lower() not in stop_w and re.search("[a-z]", w[1].lower()))
#     for w in ret:
#         print(w)
#
# from nltk.corpus import gutenberg
# fifty_bigrams(gutenberg.words("carroll-alice.txt"))

# Exercise 23
# def zipf_plot(text):
#     import pylab
#     freq = nltk.FreqDist(text)
#     sort = []
#     ranks = []
#     for w in freq.most_common(len(freq)):
#         sort.append(w[1])
#         ranks.append(len(sort))
#     pylab.plot(ranks, sort)
#     pylab.xlabel("Rank")
#     pylab.ylabel("Frequency")
#     pylab.title("Zipf Graph")
#     pylab.show()


# from nltk.corpus import gutenberg
# zipf_plot(gutenberg.words("carroll-alice.txt"))

# def random_zipf():
#     import random
#     import pylab
#     text = ""
#     for k in range(0, 100000):
#         text += random.choice("abcdefg ")
#     t_text = nltk.word_tokenize(text)
#     freq = nltk.FreqDist(t_text)
#     sort = []
#     ranks = []
#     for w in freq.most_common(len(freq)):
#         sort.append(w[1])
#         ranks.append(len(sort))
#     pylab.plot(ranks, sort)
#     pylab.xlabel("Rank")
#     pylab.ylabel("Frequency")
#     pylab.title("Random Zipf Graph")
#     pylab.show()
#
# random_zipf()

# Exercise 27
# def find_avg(type):
#     from nltk.corpus import wordnet
#     all = wordnet.all_synsets(type)
#     words = set()
#     total = 0
#     for s in all:
#         check = s.lemmas()
#         for c in check:
#             if c.name() not in words:
#                 words.add(c.name())
#                 total += len(wordnet.synsets(c.name(), type))
#     return total/len(words)
#
# print("Nouns")
# print(find_avg("n"))
# print("Verbs")
# print(find_avg("v"))
# print("Adjectives")
# print(find_avg("a"))
# print("Adverbs")
# print(find_avg("r"))

# Exercise 25
def find_language(word):
    from nltk.corpus import udhr
    ret = []
    for l in udhr.fileids():
        if l[-7:] == "-Latin1":
            if word.lower() in udhr.words(l):
                ret.append(l)
    return ret

