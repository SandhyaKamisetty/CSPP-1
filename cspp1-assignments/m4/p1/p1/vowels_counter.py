'''
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are:
 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5
@author : SandhyaKamisetty
'''
def main():
    '''
    @author : SandhyaKamisetty
    This program counts number of vowels in a string
    '''
    str_input = input()
    num_vowels = 0
    for char in str_input:
        if char in "aeiou":
            num_vowels += 1
    print(num_vowels)
    # the input string is in s
    # remove pass and start your code here

if __name__ == "__main__":
    main()
