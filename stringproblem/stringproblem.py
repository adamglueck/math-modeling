n=int(input("number of letters in string? "))
nlist=list(range(1,n+1))
d=1
e=1
totalfail="yes"
shortlist=[]
for a in range (0,n-1):
    for b in range (0,n-1-a):
        c=n-2-b-a
        list=[a,b,c,1,2,a+b,a+c,a+1,a+2,b+c,b+1,b+2,c+1,c+2,a+b+c,a+b+1,a+b+2,a+c+1,a+c+2,b+c+1,b+c+2,a+b+c+1,a+b+c+2]
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
