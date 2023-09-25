import re

str = "1 2 3 4 test strin5g6"

result = re.search("[0-9]", str) #todo: how can I use it? return true/false to check use case
resultType = type(result)
print(f"Type:{resultType}\n{result}")

result = re.findall("[0-9]", str)
resultType = type(result)
print(f"Type:{resultType}\n{result}")

s = 'A message from csev@umich.edu to cwen@iupui.edu dev.lubynets@gmail.com about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)