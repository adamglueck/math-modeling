denominator=int(input("denominator? "))
ticks=0
string=""
listy=[]
number=1
test="true"
test2="true"
while test=="true":
    if number%denominator==0:
        test="false2"
        storeticks=ticks
    string=string+str(number//denominator)
    number=10*(number%denominator)
    listy.append(number//denominator)
    if ticks==0:
        string=string+"."
    ticks=ticks+1
    if ticks>100:
        test="false"
if test=="false2":
    print(str(storeticks)+" nonrepeating digits")
print(string)
listy2=[]
lastj=0
repeater=-7
for j in range (1,len(listy)-1):
    if test2=="true":
        for i in range (1,len(listy)-j-1):
            if listy[i]==listy[i+j] and listy[i+1]==listy[i+j+1]:
                if j!=lastj:
                    repeater=(j-lastj)
                    test2="false"
                lastj=j
test4="false"
if repeater!=-7:
    print (str(repeater)+" repeating digits")
    test3="true"
    nonrep=0
    for k in range (0,repeater):
        if listy[k]!=listy[k+repeater]:
            nonrep=1+nonrep
            test4="true"
if test4=="true":
    print(str(nonrep)+" nonrepeating digits")
    
        
