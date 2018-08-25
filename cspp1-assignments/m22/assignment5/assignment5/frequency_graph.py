'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''
    determine frequency
    '''
    dict_1 = sorted(dictionary.keys())
    for i in dict_1:
        print(i, "-", "#")
    return dictionary


def main():
    '''
    main function
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
