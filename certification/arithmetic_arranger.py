import re

def arithmetic_arranger(problems, calc=False):
  if (len(problems) > 5):
    return "Error: Too many problems"

  arranged_problems = list()

  for p in problems:
    numbers = re.findall("(\d+)", p)
    operator = re.findall("[+-]", p)
    result = ""

    line = "-" * (len(max(numbers)) + 2)

    if calc:
      if operator == "+":
        result = numbers[0] + numbers[1]
      if operator == "-":
        result = numbers[0] - numbers[1]

    arranged_problems.append(
        f"{numbers[0]}\n {operator}\n {numbers[1]}\n {line}\n {result}"
    )

  return arranged_problems

r = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print(r)
