# See PyCharm help at https://www.jetbrains.com/help/pycharm/

handle = open("/home/ad/WebProjects/dev/test/testData/textFile.txt")
# fileContent = handle.read()
print("______________________________________")
# print(fileContent)
#
# print(len(fileContent))
# print(fileContent[:20])

for line in handle:
    print(line)

ar = [200, 100, 330, 190, "sdfdsf\n\r\n", "sdfdsf"]
print(ar[:1])
print(ar[:2])
str = ar[:5]
print(fr"{str}")
print(f"{str}")

xl = list()
print(type(xl))

xl.append("banana1")
xl.append("banana3")
xl.append("banana4")
xl.append("banana2")
xl.append("banana5")

print(xl)

xl.sort()

print(xl)
print(1 in xl)
print(xl[1])

print(min(xl))
del xl[1]
print(xl)

xll = [120, 300, 76786.0, 324324]

xl = xl + xll

print(xl)
xl[:]

