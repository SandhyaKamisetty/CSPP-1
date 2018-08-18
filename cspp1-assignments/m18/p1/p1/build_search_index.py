'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
import math
# helper function to load the stop words from a file
def combine_documents(document_one, document_two):
    '''
    combining documents
    '''
    dictionary = {}
    for word in document_one:
        if word in document_two:
            dictionary[word] = [document_one[word], document_two[word]]

    for word in document_one:
        if word not in dictionary:
            dictionary[word] = [document_one[word], 0]
    for word in document_two:
        if word not in dictionary:
            dictionary[word] = [0, document_two[word]]

    return dictionary
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords

def word_list(text_input):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    words = text_input.lower().strip().replace('\'', '')
    regex = re.compile('[^a-z]')
    words = regex.sub(" ", words).split(" ")
    return words

def build_search_index(docs_list):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    dictionary = {}
    stopwords = load_stopwords("stopwords.txt")
    for word in docs_list:
        word = word.strip()
        if word not in stopwords and len(word) > 0:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary

# helper function to print the search index
# use this to verify how the search index looks
def calculate_frequency(documents_values):
    '''
    frequency of values are calculated
    '''
    for key in range(len(documents_values)):
        numerator = sum([key[0] * key[1] for key in documents_values.values()])
        d1_a = math.sqrt(sum([key[0] ** 2 for key in documents_values.values()]))
        d2_a = math.sqrt(sum([key[1] ** 2 for key in documents_values.values()]))
        return numerator/(d1_a*d2_a)

def print_search_index(index):
    '''
    print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])
    document_one = build_search_index(word_list(index))
    document_two = build_search_index(word_list(index))
    dictionary = combine_documents(document_one, document_two)
    return calculate_frequency(dictionary)

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
