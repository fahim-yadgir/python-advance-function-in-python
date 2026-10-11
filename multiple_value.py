def addition(*args):
    total = 0

    for num in args:
        total = total+ num

    return total

print(addition(10,45,20))