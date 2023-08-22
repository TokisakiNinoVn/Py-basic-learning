import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == 0:
    print(">> Phuong trinh bac nhat! x =", ((-c))/b)
else:
    detal = b*b - 4*a*c
    if detal > 0:
        print(">> x1 = ", (-b) - (math.sqrt(detal))/2*a, "\t x2 = ", (-b) + (math.sqrt(detal))/2*a)
    elif detal == 0:
        print(">> Phuong trinh co nghiem kep! x = ", (-b)/2*a)
    else:
        print(">> Phuong trinh vo nghiem!")