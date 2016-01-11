# the function
def create_dict(text_file):
    """prints out how many times each word shows up in the text file"""
    
#     create an empty dictionary
    results = {}

#         loop through the list and check if the word is in the dictionary
    text = open(text_file)
    
    words = []

    for line in text:
        line = line.rstrip()
        line = line.split(" ")

        for word in line:
            if word in results:
                results[word] += 1
            else:
                results[word] = 1

    for key, value in results.iteritems():
        print key, value

    text.close()

# create_dict(x)
#         increase count +1
#         if word is not in the dictionary, add the word

#     print dictionary key-value pairs, one per line


