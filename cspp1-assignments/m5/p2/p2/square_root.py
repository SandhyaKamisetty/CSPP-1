'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''
def main():
    '''
    @author : SandhyaKamisetty
    Write a python program to find the square root of the given number
    '''
    x_i = int(input())
    epsilon = 0.01
    step = 0.1
    guess = 0.0

    while abs(guess**2-x_i) >= epsilon:
        if guess <= x_i:
            guess += step
        else:
            break

    if abs(guess**2 - x_i) >= epsilon:
        print('failed')
    else:
        print(str(guess))
    # epsilon and step are initialized
    # don't change these values
    # your code starts here

if __name__ == "__main__":
    main()
