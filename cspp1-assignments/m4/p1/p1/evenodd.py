'''
@author : SandhyaKamisetty
to print even and odd places
'''
S = "sandhya"
A1 = ""
A2 = ""
i = 0
while i < len(S):
    if i%2 == 0:
        A1 += S[i]
    else:
        A2 += S[i]
    i += 1
print("A1 =", A1)
print("A2 =", A2)
