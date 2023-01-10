name = input("Enter your name : ")
family_name = input("Enter your family name : ")
dars1 = float(input("Nomreye dars1 : "))
dars2 = float(input("Nomreye dars2 : "))
dars3 = float(input("Nomreye dars3 : "))
average = (dars1+dars2+dars3)/3
print(name, family_name)
if average >= 17:
    print("Great")
if average >= 12 and average < 17:
    print("normal")
if average < 12:
    print("fail")
