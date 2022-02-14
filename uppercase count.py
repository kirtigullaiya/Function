string="The quick Brow Fox"
def count(string):
    i=0
    count=0
    count1=0
    while i<len(string):
        if string[i]>="A" and string[i]<="Z":
            count+=1
        elif string[i]>="a" and string<="z":
            count1+=1
            # print(count)
        i+=1
    print(count)
    print(count1)
count(string)

