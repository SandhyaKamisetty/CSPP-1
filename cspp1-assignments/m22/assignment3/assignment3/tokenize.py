'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string_input):
    '''
    string frequency
    '''
    dictionary = {}
    for word in string_input:
        if word not in dictionary:
            dictionary[word] = [string_input.count(word)]
        else:
            if (string_input.count(word)) not in dictionary[word]:
                dictionary[word].append(string_input(word))
    return dictionary
            
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
