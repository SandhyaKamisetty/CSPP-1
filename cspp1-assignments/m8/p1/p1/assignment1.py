'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that
 takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.
'''

def factorial(a_n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if a_n in (0, 1):
        return 1
    return a_n * factorial(a_n-1)
    
def main():
    '''
    @author : SandhyaKamisetty
    '''
    a_n = input()
    print(factorial(int(a_n)))

if __name__ == "__main__":
    main()
