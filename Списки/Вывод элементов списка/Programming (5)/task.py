# put your python code here
n= int(input())
a=[]
b=[]
for _ in range(n):
    a.append(input())
k=int(input())
for s in range(k):
    b.append(input())
for i in range(len(a)):
    count=0
    for j in range(len(b)):
        if b[j].lower() in a[i].lower():
            count+= 1
    if count == len(b):
        print(a[i])
