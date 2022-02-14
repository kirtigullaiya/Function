# question46 of doc.
#  difference of 1 between consecutive numbers in list.
def diff():
    list=[]
    size=int(input("please enter number:"))
    i=0
    while i<size:
        ele=int(input("please enter elements:"))
        list.append(ele)
        i+=1
    print(list)
    i=0
    while i<len(list)-1:
        difference=list[i+1]-list[i]
        if difference==1:
            print("true")
        else:
            print("false")
        i+=1
        # print("true")
diff()