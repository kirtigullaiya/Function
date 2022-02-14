def bmi(hieght,weight):
    cal=weight/hieght
    if cal<=30:
        print("overwieght")
    elif cal<=25.0:
        print("normal")
    elif cal<=18.0:
        print("underweight")
    else:
        print("obese")
hieght=float(input("please enter:"))
weight=int(input("please enter:"))
bmi(hieght,weight)