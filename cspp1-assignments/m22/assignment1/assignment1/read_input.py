'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''
    text input
    '''
    no_of_lines = int(input())
    string = " "
    for _ in range(no_of_lines):
        string += input()
        string += '\n'
    print(string)


if __name__ == '__main__':
    main()
