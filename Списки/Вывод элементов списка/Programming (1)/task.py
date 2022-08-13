n= int(input())
s1 = []
s2 = []
for i in range(1,n+1):
    x=int(input())
    s1.append(x)
    x2=((x+1)**2)
    s2.append(x2)
print(*s1, sep='\n')
print()
print(*s2, sep='\n')
