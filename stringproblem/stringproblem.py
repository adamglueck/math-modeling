n=int(input("number of letters in string? "))
nlist=list(range(1,n+1))
d=1
e=1
totalfail="yes"
shortlist=[]
for a in range (0,n-1):
    for b in range (0,n-1-a):
        c=n-2-b-a
        list=[a, a+b, a+b+c, a+b+c+d, a+b+c+d+e, b, b+c, b+c+d, b+c+d+e, c, c+d, c+d+e, d, d+e, e]
        fail="no"
        for j in nlist:
            if j not in list:
                fail="yes"
        if fail=="no":
            print("works for")
            print(a,b,c,d,e)
            totalfail="no"
if fail=="yes" and totalfail=="yes":
    print("There are no combinations for which this works")
