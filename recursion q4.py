def sum_list(sum):
    if (sum)==[]:
        return 0
    else:
        return sum[0]+sum_list(sum[1:])
i=0
sum=[]
size=int(input("plaese enter size:"))
while i<size:
    num=int(input("please entr:"))
    sum.append(num)
    i+=1
print(sum_list(sum))
