# put your python code here
n= int(input())
Negatives=[]
Zeros=[]
Positives=[]
for i in range(n):
    x=int(input())
    if x<0:
        Negatives.append(x)
    if x==0:
        Zeros.append(x)
    if x>0:
        Positives.append(x)
print(*Negatives,*Zeros,*Positives, sep='\n')
