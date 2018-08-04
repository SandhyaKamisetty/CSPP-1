'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    @author : SandhyaKamisetty
    For each multiple of 3, print "Fizz" instead of the number.
    For each multiple of 5, print "Buzz" instead of the number.
    For numbers which are multiples of both 3 and 5, print "FizzBuzz"
    instead of the number.
    Read number from the input, store it in variable num.
    '''
    n_n = int(input())
    for i in range(1, n_n+1):
        if i%3 == 0:
            print("Fizz")
        if i%5 == 0:
            print("Buzz")
        if i%3 == 0 and i%5 == 0:
            print("Fizz")
            print("Buzz")

if __name__ == "__main__":
    main()
