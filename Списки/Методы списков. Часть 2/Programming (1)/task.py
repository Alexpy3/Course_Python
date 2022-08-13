# put your python code here
s= input().split()
for i in range(len(s)):
    s[i]=int(s[i])
pos_min= s.index(min(s))
pos_max= s.index(max(s))
s[pos_max], s[pos_min] = s[pos_min], s[pos_max]
print(*s)



