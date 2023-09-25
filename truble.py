mytuple = ("apple", "banana", "cherry");

print(mytuple)


listd = list([1,2,34,4,5,65,6,7,8])

print(sorted(listd))
print(sorted(listd, reverse=True))

dictt = dict({"asd1":1, "asd2":2, "asd3":4})
lst = []
for key, val in dictt.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)