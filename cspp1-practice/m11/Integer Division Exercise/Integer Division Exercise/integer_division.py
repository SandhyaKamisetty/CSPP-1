'''
#Exercise: Integer Division Exercise
#Modify the code for integer_division so that this error does not occur.
'''
def integer_division(x_n, a_s):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x_n >= a_s:
        count += 1
        x_n = x_n - a_s
    return count
def main():
    '''
    @author : SandhyaKamisetty
    '''
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
    