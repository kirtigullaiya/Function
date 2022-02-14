# question29 of doc.
# sum of multiples of 3 or 5 with limit parameter.
def multiples(limit):
    i=0
    sum=0
    sum1=0
    while i<limit:
        if i%3==0 or i%5==0:
            sum+=i
        else:
            sum1+=i
        i+=1
    print("sum of the multiples of 3 and 5:",sum)
    print("sum of the left integars:",sum1)
multiples(21)

