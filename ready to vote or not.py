# # question17 of doc--he/she can vote or not.
# def vote():
#     age=int(input("please enter age:"))
#     if age>=18:
#         print("eligible for voting.")
#     else:
#         print("not eligible.")
# vote()

def func(x=1, y=2):
    x=x+y
    y+=1
    print(x,y)
func(y=2, x=1)