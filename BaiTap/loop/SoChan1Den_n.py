
n = int(input("n: "))
    
if n > 100:
    print(">> Nhap so nho hon 100!")
else:
    for i in range(1, n, 1):
        if(i%2 == 0):
            print(">>", i)
