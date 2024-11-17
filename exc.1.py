import random
import statistics

l1: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]

print("a.a", sorted(l1, key=lambda x: len(x)))
print("a.b", sorted(l1, key=lambda x: x.count(" ")))
print("a.c", sorted(l1, key=lambda x: x[-1]))
print("a.d", sorted(l1, key=lambda x: x[::-1]))
print("a.e", sorted(l1, key=lambda x: x.count("a")))

l2: list[object] = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050,
                                                                                   "Europe"],
                    ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"],
                    ["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]

print("a.f.a", sorted(l2, key=lambda x: x[1]))
print("a.f.b", sorted(l2, key=lambda x: x[1], reverse=True))
print("a.f.c", sorted(l2, key=lambda x: x[2]))
print("a.f.d", sorted(l2, key=lambda x: (x[2], x[1])))

l3: list[int] = [random.randint(1, 100) for _ in range(50)]
print("avg", statistics.mean(l3))  # to check
print("b1", sorted(l3, key=lambda x: x))
print("b2", sorted(l3, key=lambda x: abs(x - statistics.mean(l3))))
