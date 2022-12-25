# Lambda Functions

from functools import reduce
lambda num: num * 2


def multiply(a, b): return a * b


print(multiply(2, 4))


# map(), filter(), reduce()

numbers = [1, 2, 3, 4, 5, 6]


# map()

# def double(a):
#     return a * 2

def double(a): return a * 2


result = map(double, numbers)

print(list(result))

result = map(lambda a: a * 2, numbers)

print(list(result))


# filter()

def isEven(n):
    return n % 2 == 0


result = filter(isEven, numbers)

print(list(result))

result = filter(lambda n: n % 2 == 0, numbers)

print(list(result))


# reduce()


expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

# sum = 0
# for expense in expenses:
#     sum += expense[1]

sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum)
