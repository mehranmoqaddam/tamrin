z1 = float(input("Enter zel aval: "))
z2 = float(input("Enter zel dovom: "))
z3 = float(input("Enter zel sevom: "))
if z1 < z2+z3 :
    print("Mosalas 1 : ok")
else:
    print("Mosalas 1 : not ok")
if z2 < z1+z3:
    print("Mosalas 2 : ok")
else:
    print("Mosalas 2 : not ok")
if z3 < z2+z1:
    print("Mosalas 3 : ok")
else:
    print("Mosalas 3 : not ok")