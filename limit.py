# question28 of doc.
# take parameter named as limit,no.s between 0 to limit with a label that is even or odd.
def number(limit):
    i=0
    while i<limit:
        if i%2==0:
            print(i,end="")
            print("even")
        else:
            print(i,end="")
            print("odd")
        i+=1
number(10)

