'''
@author SandhyaKamisetty
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm
# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
'''
def main():
    '''
    @author : SandhyaKamisetty
    Write a python program to find
    if the given number is a perfect cube or not
    '''
    cube_num = int(input())
    e_n = 0.01
    i_n = 1
    g_n = 0

    while g_n <= cube_num:
        if abs(g_n**3 -cube_num) < e_n:
            break
        else:
            g_n += i_n
    if abs(g_n**3 - cube_num) >= e_n:
        print(str(cube_num) + "is not a perfect cube")
    else:
        print(str(cube_num) + "is a perfect cube")
    # input is captured in s
    # watch out for the data type of value stored in s
    # your code starts here

if __name__ == "__main__":
    main()
