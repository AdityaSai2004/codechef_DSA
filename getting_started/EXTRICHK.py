a,b,c= map(int, input().split())
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
if type(area)!=complex and area>0:
    if a==b and a==c and b==c:
        print(1)
    elif a == b or b == c or c == a:
        print(2)
    else:
        print(3)
    
else:
    print(-1)
