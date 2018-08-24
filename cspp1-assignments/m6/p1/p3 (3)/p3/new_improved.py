'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    temp_int = abs(int_input)
    digi_prod = 1
    for i in range(len(str(temp_int))):
        del i
        k = temp_int%10
        digi_prod = digi_prod * k
        temp_int = temp_int // 10
    if int_input < 0:
        print('-'+str(digi_prod))
    else:
        print(digi_prod)

if __name__ == "__main__":
    main()
