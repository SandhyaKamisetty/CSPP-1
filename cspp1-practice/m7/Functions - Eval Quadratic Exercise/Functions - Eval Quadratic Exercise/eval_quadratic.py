'''
# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x),
 that returns the value of the quadratic a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.
'''

def evalquadratic(a_n, b_n, c_n, x_n):
    '''
    quadratic expression
    '''
    y_n = (a_n*(x_n**2) + (b_n*x_n) + c_n)
    return y_n
def main():
    '''
    @author : SandhyaKamisetty
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for x_n in range(len(data)):
        temp = str(data[x_n]).split('.')
        if temp[1] == '0':
            data[x_n] = int(float(str(data[x_n])))
        else:
            data[x_n] = data[x_n]
    print(evalquadratic(data[0], data[1], data[2], data[3]))
if __name__ == "__main__":
    main()
