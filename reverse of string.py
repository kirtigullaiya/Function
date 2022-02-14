string="1234abcd"
def reverse(string):
    i=1
    sum=""
    while i<len(string)+1:
        sum+=string[-i]
        i+=1
    return(sum)
print(reverse(string))
