def add_numbers_list():
    l=[50,60,10]
    l1=[10,20,23]
    i=0
    b=[]
    while i<len(l):
        sum=l[i]+l1[i]
        print(sum)
        b.append(sum)
        i+=1
    print(b)
add_numbers_list()