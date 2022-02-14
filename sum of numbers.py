a=[1,2,3,4,5]
def add(a):
    total=0
    i=0
    while i<len(a):
        total+=a[i]
        i+=1
    return total
# a=[1,2,3,4,5]

print(add(a))

# def add(a):
#     total=0
#     # i=0
#     for i in a:
#         total+=i
#     return total
# # a=[1,2,3,4,5]

# print(add((1,2,3,4,5)))