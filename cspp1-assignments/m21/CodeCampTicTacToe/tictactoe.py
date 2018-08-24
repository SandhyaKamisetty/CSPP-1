'''
@author : SandhyaKamisetty
'''
def read_input():
    '''
    input reading
    '''
    tic_tac_toe_list = []
    for _ in range(3):
        list_matrix_rows = input().strip().split()
        tic_tac_toe_list.append(list_matrix_rows)
    return list_matrix_rows


def is_valid_input(m):
    '''
    checking whether input is valid or not
    '''
    for i in m:
        for j in i:
            if j not in 'xo.':
                return 



def main():
    matrix = read_input()
    check = is_valid_input(m)





    


