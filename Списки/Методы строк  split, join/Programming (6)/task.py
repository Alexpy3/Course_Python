# put your python code here
n=input().split()
count=0
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i]==n[j]:
            count+=1
print(count)