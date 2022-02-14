list=[1,1,4,55,88,55]
b=[]
def unique(list):
    i=0
    # b=[]
    while i<len(list):
        if list[i] not in b:
            b.append(list[i])
        i+=1
    return(b)
print(unique(list))

