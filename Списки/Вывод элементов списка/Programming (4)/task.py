# put your python code here
n=int(input())
s=[]
for _ in range(n):
    s.append(input())
search=input()

for i in s:
    if search.lower() in i.lower():
        print(i)

