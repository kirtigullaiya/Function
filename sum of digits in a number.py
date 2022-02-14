# question42 of doc.
# sum of the digits will be like 1+2=3,6+7=13 etc.
def sum():    
    a=[12,67,98,34]
    b=[]
    for i in a:
        sum=0
        for j in str(i):
            sum+=int(j)
        b.append(sum)
    print(b)
sum()
