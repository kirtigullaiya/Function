# question26 of doc.
def divisible():
    num=int(input("please enter the number:"))
    if num%3==0 and num%5==0:
        print("fizz..buzz")
    elif num%3==0:
        print("fizz..")
    elif num%5==0:
        print("buzz..")
    else:
        print(num)
divisible()