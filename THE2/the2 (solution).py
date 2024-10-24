# Student name: Aly Asad Gilani
# Student ID: 2547875



a="?"
b="?"
c="?"
d="?"
check="?"

ID=input()

if ID[0] != "?": 
    a=int(ID[0])
if ID[1] != "?":
    b=int(ID[1])
if ID[2] != "?":
    c=int(ID[2])
if ID[3] != "?":
    d=int(ID[3])
if ID[5] != "?" and ID[5] !="X":
    check=int(ID[5])
elif ID[5]=="X":
        check=10


#first scenario
    
if a!="?" and b!="?" and c!="?" and d!="?" and check!="?":
    temp = ((a*2+b*3+c*5+d*7) % 11)
    if temp==check:
        print("VALID")
    else:
        print("INVALID")


#second scenario
        
elif check=="?":
    check = ((a*2+b*3+c*5+d*7) % 11)
    if check==10:
        check = "X"
    print(str(a)+str(b)+str(c)+str(d)+"-"+str(check))


#third scenario
    
else:
    if a=="?":
        a = int(((2**9)*(check-(b*3 + c*5 + d*7)))%11)
    elif b=="?":
        b = int(((3**9)*(check-(a*2 + c*5 + d*7)))%11)
    elif c=="?":
        c = int(((5**9)*(check-(a*2 + b*3 + d*7)))%11)
    elif d=="?":
        d = int(((7**9)*(check-(a*2 + b*3 + c*5)))%11)

    if check==10:
        check = "X"
    print(str(a)+str(b)+str(c)+str(d)+"-"+str(check))


        



