# 0,1,1,2,3,5,8,13,21,34
# fibonacci series meraki.
def fib(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return(fib(number-1)+fib(number-2))

number=0
while number<=10:
    if number==0:
        print(0)
    elif number==1:
        print(1)
    else:
        print((fib(number-1))+(fib(number-2)))
    number+=1

    