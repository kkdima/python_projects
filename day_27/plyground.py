def add (*args):
    print(args[1])

    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3, 4, 5))

def calculate(**kwargs):
    print(kwargs)

calculate(a=1, b=2, c=3)