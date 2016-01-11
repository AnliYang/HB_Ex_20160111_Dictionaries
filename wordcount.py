# first function
def get_list(text_file):
    """creates list of words from text file"""
#     open up the text file and format for feeding into function
    text = open(text_file)
    
    words = []

    for line in text:
        line = line.rstrip()
        line = line.split(" ")
        words = words + line

    return words

# x = get_list('twain.txt')

#     create a list of all words


# the function
def create_dict(words_list):
    """prints out how many times each word shows up in the text file"""
    
#     create an empty dictionary
    results = {}

#         loop through the list and check if the word is in the dictionary
    for word in words_list:
        if word in results:
            results[word] += 1
        else:
            results[word] = 1

    for key, value in results.iteritems():
        print key, value

# create_dict(x)
#         increase count +1
#         if word is not in the dictionary, add the word

#     print dictionary key-value pairs, one per line


