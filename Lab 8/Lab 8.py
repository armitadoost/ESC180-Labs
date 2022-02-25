# Lab 8 -- Files and Dictionaries

# Problem 1 --------------------------------------------------------------------
f = open("data2.txt")
lines = f.readlines()

check = ["Lol", "LOl","LOL","LoL","lOl","lOL","lol", "loL"]


for line in lines:
    for lol in check:
        if lol in line:
            print(line)


# Problem 2 --------------------------------------------------------------------
def dict_to_str(d):
    '''Return a str containing each key and value in dict d. Keys and values are
       separated by a comma. Key-value pairs are separated by a newline character from
       each other. For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6". (the
       order of the key-value pairs doesn’t matter and can be different every time). '''

    for key, value in d.items():
        print(str(key) + "," , str(value))


# Problem 3 --------------------------------------------------------------------
def dict_to_str_sorted(d):
    '''Return a str containing each key and value in dict d. Keys and values are
       separated by a comma. Key-value pairs are separated by a newline character from
       each other, and are sorted in ascending order by key. For example,
       dict_to_str_sorted({1:2, 0:3, 10:5}) should return "0, 3\n1, 2\n10, 5". The keys
       in the string must be sorted in ascending order.'''

    sort_key = sorted(d.items())
    for key, value in sort_key:
        print(str(key) + "," , str(value))

# Problem 4 --------------------------------------------------------------------
# Part (a)
phones = {}
f = open("vowel.txt")

for line in f:
    if line.strip():
        key, value = line.split(None, 1)
        phones[key] = value.split()

# Part (b)
phone_types = {}
d = open("type.txt")

for line in d:
    key, value = line.split()
    phone_types[key] = value

# Part (c)
def vowel_num(word):
    print(phones[word])

# Part (d)
def syllable_num(word):
    count = 0
    for a in range(len(word)):
        for b in range(len(word)):
            if word[a:b] in phone_types:
                if phone_types[word[a:b]] == "vowel":
                    count += 1

    print(count)

# Problem 5 --------------------------------------------------------------------
'''
file = open("sample.txt", "r")

def readability_lev(file):
    num_sent = 0
    num_words = 0
    num_syl = syllable_num(file)

    for line in file:
        line = line.strip("\n")
        words = line.split()
        num_sent += 1
        num_words += 1

    value = (0.39 *(num_words/num_sent)) + (11.8*(num_syl/num_words)) - 15.59
    return value
'''
if __name__ == "__main__":
    dict_to_str({1:2, 5:6})
    dict_to_str_sorted({1:2, 0:3, 10:5})
    vowel_num("AARON")
    syllable_num("AAb")