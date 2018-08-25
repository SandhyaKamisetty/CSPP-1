'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string_input):
    '''
    cleaning string
    '''
    words = string_input.lower().replace('\'', '')
    regex = re.compile('[^a-z]')
    words = regex.sub("", words)
    return words

def main():
    '''
    main function
    '''
    string_input = input()
    print(clean_string(string_input))

if __name__ == '__main__':
    main()
