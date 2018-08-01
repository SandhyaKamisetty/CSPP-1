'''
@author : SandhyaKamisetty
In this program we use while loop and for loop
'''
SUM = 0
END = 1
while END <= 6:
    SUM = SUM + END
    END = END + 1
print(SUM)

SUM = 0
for END in range(1, 7, 1):
    SUM = SUM + END
print(SUM)
