#13 reasons why

A,B,C = input().split()
temp = A
A = B
B = temp
A = int(A)*int(C)
B = int(B) + int(C)
print(A, B)
