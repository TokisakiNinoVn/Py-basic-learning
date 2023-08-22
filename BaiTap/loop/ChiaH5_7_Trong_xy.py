x = int(input("x: "))
y = int(input("y: "))

for i in range(x, y, 1):
    if i%5 == 0 or i%7 == 0:
        print(">> ", i)