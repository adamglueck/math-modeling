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
    if ticks>300:
        test="false"
if test=="false2":
    if storeticks==1:
        text="digit"
    if storeticks!=1:
        text="digits"
    print(str(storeticks)+" nonrepeating "+text)
print(string)
listy2=[]
lastj=0
repeater=-7
for j in range (1,len(listy)-4):
    if test2=="true":
        for i in range (1,len(listy)-j-4):
            if listy[i]==listy[i+j] and listy[i+1]==listy[i+j+1] and listy[i+2]==listy[i+j+2] and listy[i+3]==listy[i+j+3] and listy[i+4]==listy[i+j+4]:
                if j!=lastj:
                    repeater=(j-lastj)
                    test2="false"
                lastj=j
test4="false"
if repeater!=-7:
    if repeater==1:
        text="digit"
    if repeater!=1:
        text="digits"
    print (str(repeater)+" repeating "+text)
    test3="true"
    nonrep=0
    for k in range (0,repeater):
        if listy[k]!=listy[k+repeater]:
            nonrep=1+nonrep
            test4="true"
if test4=="true":
    if nonrep==1:
        text="digit"
    if nonrep!=1:
        text="digits"
    print(str(nonrep)+" nonrepeating "+text)
    
        
