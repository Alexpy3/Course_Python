# put your python code here
n=int(input())
s=[]

for i in range(n):
    x=int(input())
    s.append(x)
s.remove(min(s))
s.remove(max(s))
print(*s, sep='\n')