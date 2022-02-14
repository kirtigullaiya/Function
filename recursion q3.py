# 7! => 7 * 6 * 5 * 4 * 3 * 2 * 1
def pattern(num):
    if num==1:
        return 1
    else:
        return(num*pattern(num-1))

i=1
while i<=7:
    print(pattern(i))
    i+=1