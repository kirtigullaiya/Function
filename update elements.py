# question45 of doc.
# form list then if it's even add 100 or add -1
def update():
    size=int(input("please enter size:"))
    a=[]
    i=0
    while i<size:
        num=int(input("please enter number:"))
        a.append(num)
        i+=1
    print(a)
    i=0
    while i<len(a):
        if a[i]%2==0:
            print(a[i],":",a[i]+100)
        else:
            print(a[i],":",-(a[i]))
        i+=1
update()
            