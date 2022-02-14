def palindrome(string):
    if string==" ":
        return True
    elif string[0]==string[-1]:
        return palindrome(string[len(string)-1:0:-1])
    else:
        return False

list=[]
string=input("please enter:")
list.append(string)
print(list)

i=0
string=""
while i<len(list):
    j=0
    while j<len(list[i]):
        string+=list[i][j]
        j+=1
    i+=1
print(string)

# b=""
# i=1
# while i<len(string)+1:
#     b+=string[-i]
#     i+=1
# print(b)
# if b==string:
#     print("yes")
# else:
#     print("no")

# def palindrome():
#     list=[]
#     string=input("please enter:")
#     list.append(string)
#     print(list)

#     i=0
#     string=""
#     while i<len(list):
#         j=0
#         while j<len(list[i]):
#             string+=list[i][j]
#             j+=1
#         i+=1
#     print(string)

#     b=""
#     i=1
#     while i<len(string)+1:
#         b+=string[-i]
#         i+=1
#     print(b)
#     if b==string:
#         print("yes")
#     else:
#         print("no")
# palindrome()
