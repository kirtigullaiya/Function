# table in nested list.
def table():
    num=int(input("please enter num:"))
    b=[]
    c=[]
    i=1
    while i<=10:
        m=i*num
        b.append(m)
        i+=1
    c.append(b)
    print(c)
table()