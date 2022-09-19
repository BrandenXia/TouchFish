from re import compile


def triangle():
    line = [1]
    while True:
        yield line
        line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]


def expansion(n: int) -> list:
    t = triangle()
    for i in range(n):
        next(t)
    return next(t)


first = compile(r"(\w+)[ ]?\+[ ]?\w+")
second = compile(r"\w+[ ]?\+[ ]?(\w+)")


print("Enter the binomial: ", end="")
binomial = input()
print("Enter the power: ", end="")
power = int(input())

first_match = first.findall(binomial)
second_match = second.findall(binomial)

if len(first_match) == 0 or len(second_match) == 0 or len(first_match) > 1 or len(second_match) > 1:
    print("Invalid binomial")
    exit(1)

# x+1 2x+1 2x+y 2x + y 2x^2+ y y+1
match_tmp = sorted([first_match[0], second_match[0]])
first_match = match_tmp[0]
second_match = match_tmp[1]
del match_tmp
expansion_list_coefficient = expansion(power)

expansion_list_times = []
for i in range(power + 1):
    var = [power - i, i]
    expansion_list_times.append(var)

res = ""
for i in range(power + 1):
    times_tmp = expansion_list_times[i]
    coefficient_tmp = expansion_list_coefficient[i]
    upper_mark_one = "^"
    upper_mark_two = "^"
    first_match_tmp = first_match
    second_match_tmp = second_match
    first_space = " "
    second_space = " "

    if times_tmp[0] == 0:
        upper_mark_one = ""
        times_tmp[0] = ""
        first_match_tmp = ""
    if times_tmp[1] == 0:
        upper_mark_two = ""
        times_tmp[1] = ""
        second_match_tmp = ""

    if times_tmp[0] == 1:
        upper_mark_one = ""
        times_tmp[0] = ""
    if times_tmp[1] == 1:
        upper_mark_two = ""
        times_tmp[1] = ""

    if coefficient_tmp == 1:
        coefficient_tmp = ""

    if coefficient_tmp == "":
        first_space = ""
    if first_match_tmp == "":
        second_space = ""
    if second_match_tmp == "":
        second_space = ""

    if i == power:
        res += f"{coefficient_tmp}{first_space}{first_match_tmp}{upper_mark_one}{times_tmp[0]}{second_space}{second_match_tmp}{upper_mark_two}{times_tmp[1]}"
    else:
        res += f"{coefficient_tmp}{first_space}{first_match_tmp}{upper_mark_one}{times_tmp[0]}{second_space}{second_match_tmp}{upper_mark_two}{times_tmp[1]} + "
print(res)
