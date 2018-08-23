def mult_matrix(matrix_1, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    rows = len(matrix_1)
    columns = len(matrix_1[0])
    mult_matrix = generate_matrix(rows, columns)
    if len(matrix_1[0]) == len(matrix_2):
        for i in range(rows):
            for j in range(matrix_2[0]):
                for k in range(matrix_2):
                    mult_matrix[i][j] += matrix_1[i][k] * matrix_2[k][i]
        return mult_matrix
    else:
        print("Error: Matrix shapes invalid for multiplication")
        return None



def generate_matrix(rows, columns):
    add_matrix = [[0 for i in range(columns)] for j in range(rows)]
    return add_matrix

def add_matrix(matrix_1, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    rows = len(matrix_1)
    columns = len(matrix_1[0])
    add_matrix = generate_matrix(rows, columns)
    if len(matrix_1) == len(matrix_2) and len(matrix_1[0] == len(matrix_2[0]):
        for i in range(row):
            for j in range(columns):
                add_matrix[i][j] += matrix_1[i][j] + matrix_2[i][j]
        return add_matrix
    else:
        print("Error: Matrix shapes invalid for addition")
        return None

def read_matrix(matrix_1, matrix_2):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix_list = []
    list_input = input().split(',')
    rows, columns = int(list_input[0]), int(list_input[1])
    for _ in range(rows):
        list_matrix_rows = input().split()
        if columns == len(list_matrix_rows):
            matrix_list.append(int(i) for i in list_matrix_rows)
        else:
            print("Error: Invalid input for the matrix")
            return None 
    
def main():
    # read matrix 1
    matrix_1 = read_matrix()
    if matrix_1 is None:
        exit()


    # read matrix 2
    matrix_2 = read_matrix()
    if matrix_2 is None:
        exit()

    # add matrix 1 and matrix 2
    print(add_matrix(matrix_1, matrix_2))

    # multiply matrix 1 and matrix 2
    print(mult_matrix(matrix_1, matrix_2))

if __name__ == '__main__':
    main()
