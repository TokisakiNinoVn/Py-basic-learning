name = 'Tokisaki Nino'
name_ = "Hoshino Nino"
addName = name + name_
lastName = 'Nino'
lastName_ = 'nino'
firstName = 'Tokisaki'

a = lastName in name # >> true
a_ = lastName_ in name # >> false
b = lastName not in name
cutName = addName[0:13]
# print(not a) # >> false
# print(b) # >> false
# print(addName)
# print(addName[0:13])
# print(name == name_)
# print(lastName == addName[0:12], addName)
# print(cutName, cutName == name)
# print(firstName != lastName)
print(lastName_ not in name)
