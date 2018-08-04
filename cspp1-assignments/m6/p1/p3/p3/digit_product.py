'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    @author : SandhyaKamisetty
    Given a  number int_input, find the product of all the digits
    Read any number from the input, store it in variable int_input.
    '''
    n_s = 123
    temp = 1
    i = 0
    while i < n_s:
        temp = temp*i
        i = i+1
    print(temp)


if __name__ == "__main__":
    main()
