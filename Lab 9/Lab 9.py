# Lab 9

# Problem 1
# Part (a)
text = open("text.txt", encoding="latin-1").read().split()
word_counts = {}


##

# Problem 1a

# f = open("text.txt", encoding="latin-1").read()
# words = f.split() #list of all words

words = ["I", "am", "a", "sick", "man.", "I", "am", "a", "spiteful", "man.", "I", "am",
"an", "unattractive", "man.", "I", "believe", "my", "liver", "is", "diseased.",
"However,", "I", "know", "nothing", "at", "all", "about", "my", "disease,", "and",
"do", "not", "know", "for", "certain", "what", "ails", "me."]


def word_count(words):
'''Take in list of words and return dictionary of word count'''
    word_counts = {}
    for word in words:
        if word in word_counts.keys(): #word has already been found at least once
            word_counts[word] += 1
        else: #coming across new word for the first time
            word_counts[word] = 1
    return word_counts

answer = {"sick": 1, "man.": 3, "at": 1, "what": 1, "nothing": 1, "do": 1, "is": 1, "me.": 1,
"I": 5, "ails": 1, "an": 1, "am": 3, "know": 2, "disease,": 1, "not": 1, "liver": 1,
"believe": 1, "all": 1, "my": 2, "certain": 1, "However,": 1, "and": 1, "for": 1,
"unattractive": 1, "spiteful": 1, "about": 1, "a": 2, "diseased.": 1}


## Problem 1b

def top10(L):
    new_L = L.sort() #sorts list in increasing order
    return new_L[-10:] #accesses last 10, which are the largest

## Problem 1c

def swap_dict(d): #swaps values with keys of a dictionary
    new_d = {}
    for key, value in d.items():
        #print(key, value)
        new_d[value] = key
    return new_d

def top10words(words):
    '''Take in list of words and return top 10 used ones'''
    L = []
    freq = word_count(words) #makes dictionary with word counts
    #print(freq)
    inv_freq = swap_dict(freq) #swaps keys & values (freq=key,word=value)
    sorted_freq = dict(sorted(inv_freq.items())) #list of increasing freq

    for i in sorted_freq.values():
        L.append(i) #list of all words in order of most used

    return L[-10:] #prints top 10 words with highest freq

text = open("prideandprejudice.txt", encoding="latin-1").read()
# print(text)
words = text.split() #splits all text by spaces (i think)
# print(words[:20]) #prints first 20 words to see if it works
print(top10words(words))

#both returning different values?? \\ seems weird too

## Problem 2

#copied and pasted raw code into a text file
#converted text file to pure text with Format
#made modifications to text file
#saved text file with a .html extension
#opened file

## Problem 3

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

f = urllib.request.urlopen("https://ca.search.yahoo.com/search?p=university+of+toronto&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8/")
#will display Yahoo results source page for searching 'engineering science' (doesn't work tho)

page = f.read().decode("utf-8")
f.close()
#print(page)
page.split('<span>')

def results(term):
    '''Return number of search results by searching a term, or keyword'''
    template = "https://ca.search.yahoo.com/search?p=" + term.replace(" ", "+") + "&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8/"

    f = urllib.request.urlopen(template)
    page = f.read().decode("utf-8")
    f.close()
    for result in page.split('<span>'):
        if ",000 results" in result.split('<\span>')[0]:
        num_results = result.split('<\span>')[0].split()[0]
        num_results = num_results.replace(',', '') #takes away commas
        num_results = int(num_results)
    return num_results

def choose_variant(variants):
    '''Take in a list of variants/key search teams and return whichever one will
    have the most search results'''
    d = {}
    for v in variants:
        d[v] = results(v)
        #print(d.items())
    return max(d, key=d.get) #returns key that corresponds to max value (probably)
