import time
x = time.localtime()

birthYear = int(input("Nam sinh: "))
year = x[0]

# print(x)
print(">> ",year-birthYear, " tuoi")