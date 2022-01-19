n=int(input())
l_e=[]
l_o=[]
for i in range(1,n+1):
    a=2*i
    l_e.append(a)
    l_o.append(a-1)

print(sum(l_o),sum(l_e))
