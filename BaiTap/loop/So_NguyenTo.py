x = int(input("x: "))

def KT_nguyenTo(n):
    dem = 0
    for i in range(1, n+1):
        if n%i == 0:
            dem += 1
    
    if dem == 2:
        return 1
    else:
        return 0
    
if KT_nguyenTo(x) == 1:
    print(f">> {x} La so nguyen to!")
else:
    print(f">> {x} Khong la so nguyen to!")