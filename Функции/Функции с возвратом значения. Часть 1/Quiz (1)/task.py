#  You can experiment here, it won’t be checked
def do_something(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result
print(do_something([2, 2, 2, 2]))