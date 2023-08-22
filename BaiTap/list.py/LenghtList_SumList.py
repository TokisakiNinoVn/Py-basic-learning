listNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# count = 0
# sum = 0
# for i in listNumber:
#     count += 1
#     sum += i
# print(f">> Count: {count}")
# print(f">> Count Librali: {len(listNumber)}")
# print(f">> Sum: {sum}")

# listEven = []
# # listEven = [] * (len(listNumber))
# listOdd = []
# for i in listNumber:
#     if i%2 == 0:
#         listEven.append(i)
#     if i%2 == 1:
#         listOdd.append(i)
# print(listEven)
# print(listOdd)


# newList = []
# newList.append(listNumber[2])
# newList.append(listNumber[5])

# print(newList)
# for i in newList:
#     print(f">> {i}")
# print(newList[0])
# print(newList[1])

childList = []
## Case 1:
# for i in listNumber:
#     childList.append(i)
# print(childList)


##Case 2:
# for i in range(len(listNumber)):
#     if (listNumber[1]) >= 4 or (listNumber[i] <= 6):
#         childList.append(i)
# print(">> ", childList)

## Case 3:
for i in range(len(listNumber)):
    if (listNumber[1]) >= 4 or (listNumber[i] <= 6):
        childList.insert(0, i)
print(">> ", childList)
