x = int(input("x: "))
y = int(input("y: "))

for i in range(x, y, 1):
    if i%2 == 0 and i%3 == 0:
        print(">> ", i)