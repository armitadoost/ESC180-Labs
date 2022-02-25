def wordCount(sentences):
    d = {}
    w = {}
    for x in range(len(sentences)):
        for word1 in sentences[x]:
            if word1 in d:
                w = d[word1]
            else:
                w = {}
            for word2 in sentences[x]:
                if word1 != word2 and word2 not in w:
                    w[word2] = 1
                elif word2 in w:
                    w[word2] += 1

            d[word1] = w



    return d

d = wordCount([["i", "am", "a", "sick", "man"],
["i", "am", "a", "spiteful", "man"]])  # assign the return value to a variable
print(d)


# make a dictonary of all the words in the entire list
# see what words are also in the sentence it appears on
