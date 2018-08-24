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
    '''
    checking the game rules
    '''
    x_count = 0
    o_count = 0
    for row in matrix:
        x_count += row.count('x')
        o_count += row.count('o')
        if o_count > 5 or x_count > 5:
            return False
    return True

def check_rows_columns(matrix, check_var):
    '''
    checking rows and columns
    '''
    for row in matrix:
        if len(set(row)) == 1 and row[0] == check_var:
            return False
    return True

def new_transpose_matrix(matrix, increment, temp_matrix):
    '''
    transpose of matrix
    '''
    if increment == len(matrix):
        return temp_matrix
    else:
        temp_matrix.append([matrix[0][increment], matrix[1][increment], matrix[2][increment]])
        return new_transpose_matrix(matrix, increment+1, temp_matrix)

def decide_winner(matrix, winner_var):
    '''
    deciding winner
    '''
    transpose_matrix = new_transpose_matrix(matrix, 0, [])
    if is_valid_game(matrix, winner_var) or\
       is_valid_game(transpose_matrix, winner_var):
        return True
    elif (matrix[0][0] == matrix[1][1] == matrix[2][2] == winner_var) or\
        (matrix[0][2] == matrix[1][1] == matrix[2][0] == winner_var):
        return True
    else:
        return False

def main():
    '''
    main function
    '''
    tic_tac_toe_list = read_input()
    if is_valid_input(tic_tac_toe_list):
        if is_valid_game(tic_tac_toe_list):
            if decide_winner(tic_tac_toe_list, 'x'):
                print('x')
            elif decide_winner(tic_tac_toe_list, 'o'):
                print('o')
            else:
                print('draw')
    else:
        print("invalid input")

main()
