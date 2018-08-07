'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that
 takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.
'''

def factorial(a):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if a == 1 or a == 0:
        return 1
    else:
        return (a * factorial(a-1))
    
def main():
    '''
    @author : SandhyaKamisetty
    '''
    a = input()
    print(factorial(int(a)))

if __name__== "__main__":
    main()
