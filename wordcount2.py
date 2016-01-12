import sys
import re
import collections


def create_dict(argv):
    """prints out how many times each word shows up in the text file"""
    
#     create an empty dictionary
    results = {}
    results2 = []

#         loop through the list and check if the word is in the dictionary
    text = open(argv)

    for line in text:
        line = line.rstrip()
        line = line.split(" ")

        for word in line:
            word = word.translate(None, '~!@#$%^&*()_+<>?:"{}|/.,\';\][=-]')
            word = word.lower()
            results2.append(word)

            # if word in results:
            #     results[word] += 1
            # else:
            #     results[word] = 1

    results2 = collections.Counter(results2)

    # for key, value in results.iteritems():
    #     print key, value
    for word in results2:
        print word, results2[word]

    text.close()
print sys.argv
create_dict(sys.argv[1])
# create_dict(x)
#         increase count +1
#         if word is not in the dictionary, add the word

#     print dictionary key-value pairs, one per line


