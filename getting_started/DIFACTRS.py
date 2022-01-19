n=int(input())
li=[]
for i in range(1,n+1):
    if n%i==0:
        li.append(i)
print(len(li))
for i in range(len(li)):print(li[i],end=' ')
