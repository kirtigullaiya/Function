

def my_func():
    print("i love")
s="myself"
my_func()
print(s)

def my_func(max):
    num=[3,5,7,34,2,89,2,5]
    i=0
    while i<len(num):
        if max<num[i]:
            max=num[i]
        i+=1
    print(max)
my_func(0)