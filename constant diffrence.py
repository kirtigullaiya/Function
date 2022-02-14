# question47 of doc.
# constant diffrence between elements.
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
    num=int(input("please enter number:"))
    while i<len(list)-1:
        difference=list[i+1]-list[i]
        if difference==num:
            c=difference
        i+=1
    print("the constant difference between elements of list:",c)
diff()