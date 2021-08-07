def fibonacci_sequence():
    n1 = 0
    n2 = 1
    while True:
        yield n2
        n2 = n1 + n2
        n1 = n2 -n1

for number in fibonacci_sequence():
    if number > 200:
        break
    print(number)
