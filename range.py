numbers = [5, 2, 0, 20, 30]
for number in numbers:
    if number == 0:
        print("The number you gave is 0")
        continue
    new_number = 100/number
    division = "100/{} = {}"
    print("", division.format(number, new_number))
