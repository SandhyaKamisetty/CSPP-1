'''
#Exercise: Assignment-2
#Implement the updateHand function. Make sure
 this function has no side effects: i.e., it must not
  mutate the hand passed in. Before pasting your function
   definition here, be sure you've passed the appropriate tests in test_ps4a.py.
'''
import copy
def updatehand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    temp_hand = copy.deepcopy(hand)
    for key in word:
        temp_hand[key] = temp_hand[key] - 1
    return temp_hand

def main():
    '''
    @author : SandhyaKamisetty
    '''
    num_n = input()
    adict = {}
    for i in range(int(num_n)):
        del i
        data = input()
        len_n = data.split()
        adict[len_n[0]] = int(len_n[1])
    data1 = input()
    print(updatehand(adict, data1))

if __name__ == "__main__":
    main()
