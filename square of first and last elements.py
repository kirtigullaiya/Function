def square():
    l=[]
    k=[]
    i=1
    while i<=30:
        if i<=5:
            square=i**2
            l.append(square)
        i+=1
    i=25
    m=[]
    while i<=30:
        if i<=30:
            square1=i**2
            m.append(square1)
        i+=1
    k.append(l)
    k.append(m)
    
    print(l)
    print(m)
    print(k)
square()

        