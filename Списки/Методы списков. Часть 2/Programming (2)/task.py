# put your python code here
s=input().lower().split()
cnt1= s.count('a')
cnt2= s.count('an')
cnt3= s.count('the')
s2=cnt1 + cnt2 + cnt3
print('Общее количество артиклей:',s2)
