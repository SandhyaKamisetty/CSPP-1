'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''
    sorting of keys
    '''
    keys_in_dict = sorted(dictionary)
    for i in keys_in_dict:
        print(i, "-", dictionary[i])

def main():
    '''
    main function
    '''
    dictionary = input()
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
