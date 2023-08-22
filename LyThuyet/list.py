listA = ['Tokisaki', 'Nino', '02112004', 'Hoshino Ai']
listB = ["Tokisaki Nino", 0, 2, 1, 1, 2, 0, 0, 4, "Hoshino Ai"]
listNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(listA[1])
fullName = "Tokisaki Nino"

# print(fullName == listB[0])
# print(fullName in listB[0])
# print(listB[0:4+1])

# for i in listA:
#     print(f">> {i}")

# print(">> ",listA[-1])

# >> Replace/remote
# listB[1:9] = ['Namae Wa Tokisaki Nino!', 'Hiii']
# print(">> ",listB)
# listNumber[1:2] = []
# print(">> ",listNumber)

## >> insert
x = 'Insert'
y = 2004
listNumber.append(x)
# print(">> ",listNumber)
listNumber.insert(0, y)
print(">> ",listNumber)

# # >> Remote
# del listNumber[-1]
# print(">> ",listNumber)
# del listNumber[0: 4]
# print(">> ",listNumber)

listNumber.remove(2004)
print(">> ",listNumber)
# listNumber.remove("Tokisaki Nino") # >> Error
listNumber.remove("Insert")
print(">> ",listNumber)