'''
#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts
 with the player. We'll be implementing the playHand function.
  This function allows the user to play out a single hand. First,
   though, you'll need to implement the helper calculateHandlen function,
    which can be done in under five lines of code.
'''
def calculatehandlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    length = 0
    for key in hand:
        length = length + (hand[key])
    return length
def main():
    '''
    @author : SandhyaKamisetty
    '''
    n_s = input()
    adict = {}
    i = 0
    for i in range(int(n_s)):
        del i
        data = input()
        l_s = data.split()
        adict[l_s[0]] = int(l_s[1])
    print(calculatehandlen(adict))
if __name__ == "__main__":
    main()
