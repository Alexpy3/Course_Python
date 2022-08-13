# put your python code here
n=int(input())
s=[]
for i in range(n):
    a=input()
    s.append(a)
k = int(input())
x1=''
x2=''
for j in range(n):
    if len(s[j]) >= k:
        x1 = s[j][k - 1]
        x2+=x1
print(x2)

