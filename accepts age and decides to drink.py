
def drink():
    age=int(input("please enter the age:"))
    if age<=14:
        print("drink toddy.")
    elif age<=18:
        print("drink coke.")
    elif age<21:
        print("drink beer.")
    elif age>=21:
        print("drink whisky.")
    else:
        print("invalid")
drink()
