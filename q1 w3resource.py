# def max():
#     list=[3,6.-5]
#     i=0
#     max=0
#     while i<len(list):
#         if max<list[i]:
#             max=list[i]
#         i+=1
#     print(max)
# max()

def sum(list):
    list=[8,2,3,0,7]
    sum=0
    i=0
    while i<len(list):
        sum+=list[i]
        i+=1
    print(sum)
# sum(list) 

def multiply():
    a=[8,2,3,-1,7]
    i=0
    k=1
    while i<len(a):
        k*=a[i]
        i+=1
    print(k)
# multiply()

# factorial.
def factorial():
    number=int(input("please enter:"))
    i=number-1
    sum=0
    while i>=0:
        c=i*number
        print(c)
        sum+=c
        i-=1
    
    print(sum)
factorial()

# perfect no question11.
def perfect_no(per):
    i=1
    sum=0
    while i<per:
        if per%i==0:
            sum+=i
            # print(sum)
        i+=1
    if sum==per:
        print("yes")
    else:
        print("no")
per=int(input("please enter the number:"))
perfect_no(per)

# palindrome question12.
def palindrome(string):
    i=1
    sum=""
    while i<len(string)+1:
        sum+=string[-i]
        i+=1
    # print(sum)
    if sum==string:
        print("yes")
    else:
        print("no")
string=input("please enter string:")
palindrome(string)

