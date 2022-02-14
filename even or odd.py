# question49 of doc.
# input n numbers and find is it even or odd.
def even():
    n=int(input("please enter number:"))
    i=0
    while i<n:
        n1=int(input("please enter numbers::"))
        if n1%2==0:
            print("even",n1)
        else:
            print("odd",n1)
        i+=1
even()