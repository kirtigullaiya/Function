# add with recursion.
def pattern(num):
    if num==1:
        return(1)
    else:
        return(pattern(num-1))+3
i=1
while i<10:
    print(pattern(i))
    i+=1