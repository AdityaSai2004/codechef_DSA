n=int(input())
if n%5==0 or n%11==0:
    if n%55!=0:
        print("ONE")
    else:
        print("BOTH")
else:
    print("NONE")
