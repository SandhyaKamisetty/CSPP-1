#Guess My Number Exercise
'''
@author : SandhyaKamisetty
this program guesses the Number
'''
def main():
    mid_num = 0
    mid_num = 50
    max_num = 100
    guess = "Is your secret number: "
    print("please think of a number between 0 and 1001")
    print(guess + str(mid_num) + "?")
    request = input("enter 'h' to indicate the guess is too high.")
    while request != 'c':
        if request == 'h':
            min_num = mid_num
            mid_num = int((mid_num + max_num)/2)
        elif request == '1':
            max_num = mid_num
            mid_num = int((mid_num + min_num)/2)
        else:
            print("sorry, I did not understand your input.")
        print(guess + str(mid_num) + "?")
        request = input("enter 'h' to indicate the guess is too high.")
    if request == 'c':
        print("game over. your secret number was:" + str(mid_num))
    #your code here

if __name__ == "__main__":
    main()