sen: str = "This chocolate cake is rich, moist, and full of delicious chocolate flavor.\
 To make the cake, you will need chocolate, flour, sugar, eggs, and butter.\
 After baking the chocolate cake, let the cake cool before adding the chocolate frosting."
l1: list[str] = sen.lower().replace(".", "").replace(",", "").split()
dict1: dict[str, int] = {}
print(l1)  # to check
for i in l1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)  # to check
max_value1: int = None
max_word1: str = None

for i in dict1:
    if max_value1 is None or max_value1 < dict1.get(i, 0):
        max_value1 = dict1.get(i, 0)
        max_word1 = i
    else:
        continue
print(max_word1, max_value1)

dict2: dict[str, int] = {}
for i in sen.replace(" ", ""):
    if i in dict2:
        dict2[i] += 1
    else:
        dict2[i] = 1

print(dict2)  # to check

max_value2: int = None
max_word2: str = None

for i in dict2:
    if max_value2 is None or max_value2 < dict2.get(i, 0):
        max_value2 = dict2.get(i, 0)
        max_word2 = i
    else:
        continue
print(max_word2, max_value2)
