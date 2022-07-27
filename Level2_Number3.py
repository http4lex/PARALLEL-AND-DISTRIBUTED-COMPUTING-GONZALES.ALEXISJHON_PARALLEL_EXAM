a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]

def getIndex(n):
    for i in range(len(b)):
        if n==b[i]:
            return i

def getLetter(index):
    for i in range(len(a)):
        if index==i:
            return a[i]

userinput=int(input("Enter an integer between 0 and 35: "))
if userinput>0 and userinput<=35:
    if userinput<=9:
        print(userinput)
    else:
        index=getIndex(userinput)
        print(getLetter(index).upper())
else:
    print("you must input Only number 0-35")
