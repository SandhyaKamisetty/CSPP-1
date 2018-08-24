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


def is_valid_input(matrix):
    '''
    checking whether input is valid or not
    '''
    for row in matrix:
        for element in row:
            if element not in 'xo.':
                return False
        return True
def is_valid_game(matrix):
    x_count = 0
    o_count = 0
    for row in matrix:
        x_count += row.count('x')
        o_count += row.count('o')
        if o_count > 5 or x_count > 5:
            return False
    return True

def check_rows_columns(matrix, check_var):
    for row in matrix:
        if len(set(row) == 1 and row[0] ==check_var):
            return False
    return True

def new_transpose_matrix(matrix, increment, temp_matrix):
    if increment == len(matrix):
        return temp_matrix
    else:
        temp_matrix.append([matrix[0][increment], matrix[1][increment], matrix[2][increment]])
        return new_transpose_matrix(matrix, increment+1, temp_matrix)

def decide_winner(matrix, winner_var):
    transpose_matrix = new_transpose_matrix(matrix, 0, [])
    if is_valid_game(matrix, winner_var) or\
        is_valid_game(transpose_matrix, winner_var) or\
        matrix[0][0] == matrix[1][1] == matrix[2][2] == check_var or\
        matrix[0][2] == matrix[1][1] == matrix[2][0] == check_var
        return True
    return False





def main():
    matrix = read_input()
    if is_valid_input(matrix):
        if is_valid_game(matrix):
            if is_winner(matrix, 'x'):
                print('x')
            elif decide_winner(matrix, 'o'):
                print('o')
            else:
                print('draw')
    else:
        print("invalid input")

    






    


