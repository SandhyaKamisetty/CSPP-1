'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
DICT_NUM = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14,
            '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def card_ranks(cards):
    '''
    return a sorted list of ranks
    '''
    ranks = ['--23456789TJQKA'.index(f) for f, s in cards]
    ranks.sort(reverse=True)
    return ranks
#def get_face_values(hand):
   # '''
    #return face value
    #'''
    #face_values = [DICT_NUM[f] for f, suit_val in hand]
    #return face_values
#def get_suit_values(hand):
    #'''
    #return suit value
    #'''
    #suit_values = [s for f, s in hand]
    #return suit_values

def kind(count, ranks):
    '''
    Return all three kind, four kind, one pair.
    '''
    for rank in ranks:
        if ranks.count(rank) == count:
            return rank
    return None

def is_two_pair(ranks):
    '''
    return two is_two_pair
    '''
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

def is_straight(ranks):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    suits = [s for f, s in hand]
    return len(set(suits)) == 1

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush
    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    return_value = None
    ranks = card_ranks(hand)
    if is_straight(ranks) and is_flush(hand):
        return_value = (8, max(ranks))
    elif kind(4, ranks):
        return_value = (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return_value = (6, kind(3, ranks), kind(2, ranks))
    elif is_flush(hand):
        return_value = (5, ranks)
    elif is_straight(ranks):
        return_value = (4, max(ranks))
    elif kind(3, ranks):
        return_value = (3, kind(3, ranks), ranks)
    elif is_two_pair(ranks):
        return_value = (2, is_two_pair(ranks), ranks)
    elif kind(2, ranks):
        return_value = (1, kind(2, ranks), ranks)
    else:
        return_value = (0, ranks)
    return return_value
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        hand_list = line.split(" ")
        HANDS.append(hand_list)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
