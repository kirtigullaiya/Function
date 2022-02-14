# question32 of doc.
# returns a list of all the powers of 2 with the exponent ranging from 0 to n.
def power():
    l=[]
    size=int(input("please enter size:"))
    i=0
    while i<size:
        num=int(input("please enter number:"))
        square=2**num
        if square%2==0 or square%2==1:
            l.append(square)
        i+=1
    print(l)
power()
