'''
@author : SandhyaKamisetty
This program evaluates two variables
'''
VAR_A = 19
VAR_B = 18
if (isinstance(VAR_A, str) or isinstance(VAR_B, str)):
    print("string involved")
elif VAR_A > VAR_B:
    print("bigger")
elif VAR_A == VAR_B:
    print("equal")
else:
    print("smaller")
