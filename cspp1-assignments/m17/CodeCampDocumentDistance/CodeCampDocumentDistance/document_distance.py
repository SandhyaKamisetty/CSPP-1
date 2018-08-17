'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
def combine_dictionaries(dictionary_str1, dictionary_str2):
    '''
    str2 dictionaries are combined
    '''
    dictionary = {}
    for word in dictionary_str1, dictionary_str1:
        if word in dictionary_str2:
            dictionary[word] = [dictionary_str1[word], dictionary_str2[word]]

    for word in dictionary_str1:
        if word not in dictionary:
            dictionary[word] = [dictionary_str1[word], 0]
    for word in dictionary_str2:
        if word not in dictionary:
            dictionary[word] = [0, dictionary_str2[word]]
    return dictionary

def calculate_similarity(dictionary_values):
    '''
    calculating frequency
    '''
    numerator = sum([k[0] * k[1] for k in dictionary_values()])
    d1_a = math.sqrt(sum([k[0] ** 2 for k in dictionary_values()]))
    d2_a = math.sqrt(sum([k[1] ** 2 for k in dictionary_values()]))
    return numerator/(d1_a*d2_a)
def create_dictionary(words_list):
    '''
    returns dictionary, takes input as word list
    '''
    dictionary = {}
    stopwords = load_stopwords("stopwords.txt")
    for word in words_list:
        word = word.strip()
        if word not in stopwords and len(word) > 0:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary

def clean_given_text(text_input):
    '''
    takes str1ing and return list
    '''
    words = text_input.lower().strip().replace('\'', '')
    regex = re.compile('[^a-z]')
    words = regex.sub(" ", words).split(" ")
    return words
def similarity(text_1, text_2):
    '''
    Compute the document distance as given in the PDF
    '''
    dictionary_str1 = clean_given_text(text_1)
    dictionary_str2 = clean_given_text(text_2)
    dictionary = combine_dictionaries(dictionary_str1, dictionary_str2)
    return calculate_similarity(dictionary)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename_n:
        for line in filename_n:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take str2 inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
