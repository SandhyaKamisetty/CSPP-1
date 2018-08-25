'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string_input):
    '''
    string frequency
    '''
    dictionary = {}
    for word in string_input:
        if word in dictionary:
            dictionary[word] += 1
        elif word not in dictionary:
            dictionary[word] = 1
    return dictionary
def clean_string(string_input):
    '''
    cleaning string
    '''
    words = re.sub('[^a-z]', " ",replace('\'', '')).split(" ")
    return word

def main():
    '''
    main function
    '''
    string_input = []
    lines = int(input())
    for i in range(lines):
        string_input.append(input())
        i += 1
    print(tokenize(string_input))

if __name__ == '__main__':
    main()
