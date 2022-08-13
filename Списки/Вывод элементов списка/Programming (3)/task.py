# put your python code here
n = int(input())
s = []
for i in range(n):
    st=input()
    if st not in s:
        s.append(st)
print(*s, sep='\n')
