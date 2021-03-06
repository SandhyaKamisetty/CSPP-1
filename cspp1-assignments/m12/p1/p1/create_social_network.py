'''
    Assignment-1 Create Social Network
    @author : SandhyaKamisetty
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
    dict_input = {}
    for i in range(0, len(data), 2):
        if data[i] not in dict_input:
            dict_input[data[i]] = data[i+1].split(",")
    return dict_input

def main():
    '''
        handling testcase input and printing output
    '''
    num_n = int(input())
    list_n = []
    for i in range(num_n):
        data_input = input().split(" ")
        list_n.extend(data_input)
    print(create_social_network(list_n))

if __name__ == "__main__":
    main()
