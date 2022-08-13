# put your python code here
L, M = input().split(), input().split()
print(*(int(L[i])+int(M[i]) for i in range(len(L))))



