dict1: dict[int, int] = {}
for i in range(1, 21):
    dict1[i] = i ** 3
print(dict1)  # to check

x: int = int(input("enter a number: "))
print(f"{x}**3 = {dict1.get(x, "not in the dictionary")}")
