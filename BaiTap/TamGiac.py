a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# print(a, "\t", b, "\t", c)
if a + b > c and a + c > b and b + c > c:
    print("Tam giac?\t>>[True]")
    if a == b and c != a or b == c and c != a or c == a and c != b:
        print("Tam giac can")
    elif a == b and b == c and c == a:
        print("Tam giac deu")
    else:
        print("Tam giac thuong")
else:
    print("Tam giac?\t>>False")



