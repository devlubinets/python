import re


def arithmetic_arranger(problems, calc=False):
    arranged_problems = dict()

    if (int(len(problems)) > 5):
        return "Error: Too many problems."

    for p in problems:
        numbers = re.findall("(\d+)", p)

        if not all(n.isdigit() for n in numbers):
            return "Error: Numbers must only contain digits."

        if int(len(numbers[0])) > 4 or int(len(numbers[1])) > 4:
            return "Error: Numbers cannot be more than four digits."

        operator = re.findall("[+-]", p)

        if len(operator) == 0:
            return "Error: Operator must be '+' or '-'."

        result = ""
        line = "-" * (len(max(numbers)) + 2)

        if calc:
            if operator == "+":
                result = numbers[0] + numbers[1]
            if operator == "-":
                result = numbers[0] - numbers[1]

        arranged_problems["x"] = numbers[0]
        arranged_problems["y"] = f"{operator} {numbers[1]}"
        arranged_problems["line"] = line
        arranged_problems["result"] = result

    arranged = list()

    for x in arranged_problems["x"]:
        arranged.append(x)
    for y in arranged_problems["y"]:
        arranged.append(y)
    for line in arranged_problems["line"]:
        arranged.append(line)
    for result in arranged_problems["result"]:
        arranged.append(result)

    return arranged_problems


r = arithmetic_arranger(["3801 - 2", "123 + 49"])
print(r)
