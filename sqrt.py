def sqrt(num: int):
    a = 0
    b = 1
    increase = 1
    while True:
        decision = a ** 2 < num < b ** 2
        if increase == 0.00000000000001:
            return a
        elif num == a ** 2:
            return a
        elif num == b ** 2:
            return b
        elif decision:
            increase /= 10
            b = a + increase
            print(a, "and", b)
        else:
            a += increase
            b += increase
            print(a, "and", b)


while True:
    number = int(input())
    a = sqrt(number)
    print(a)