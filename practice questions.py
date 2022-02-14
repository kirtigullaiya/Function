# factorial number.
def func(i):
# i=int(input("please enter:"))
    fac=1
    while i>0:
       fac=fac*i
       i-=1
    print(fac)
func(6)