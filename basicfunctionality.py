# this is a commented line

from enum import Enum
name = "Beau"  # this is an inline comment
print(type(name) == str)
print(isinstance(name, str))  # True

age = 39
print(isinstance(age, int))  # True
print(isinstance(age, float))

age = float(39)
print(isinstance(age, float))

age = float("39")
print(isinstance(age, float))

# age = int(name) # creates error
# print(isinstance(age, int))

print(1 + 1)  # 2
print(1 + -1)  # 0
print(2 - 1)  # 1
print(2 * 2)  # 4
print(4 / 2)  # 2.0
print(4 % 3)  # 1
print(4 ** 2)  # 16
print(5 // 2)  # 2

print(0 or 1)  # 1
print(False or 'hey')  # 'hey'
print('hi' or 'hey')  # 'hi'
print([] or False)  # 'False'
print(False or [])  # '[]'

print(0 and 1)  # 0
print(1 and 0)  # 0
print(False and 'hey')  # False
print('hi' and 'hey')  # 'hey'
print([] and False)  # []
print(False and [])  # False


def is_adult(age):
    if age > 18:
        return True
    else:
        return False


def is_adult2(age):
    return True if age > 18 else False


name = "Beau"
name += " is my name"
age = str(39)
print(name)
print("""Beau is

39

years old
	""")

print("bEAu".upper())
print("bEAu person".title())
print("bEAu person".islower())
print("beau person".islower())

print(name.lower())
print(name)
print(len(name))

print("au" in name)
print("aU" in name)

print("Be\"au")
print('Be"\'au')
print('Be\nau')
print('Be\\au')

print(name[0])
print(name[-1])
print(name[1:3])
print(name[:3])
print(name[1:])

done = True
done = -1
if done:
    print("yes")
else:
    print("no")

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
print(read_any_book)

read_any_book = all([book_1_read, book_2_read])
print(read_any_book)

num1 = 2+3j
num2 = complex(2, 3)

print(num2.real, num2.imag)

print(abs(5.5))
print(abs(-5.5))
print(round(5.49))
print(round(5.5))
print(round(5.500101010, 1))


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State.ACTIVE)
print(State.ACTIVE.value)
# print(State[1])
print(State['ACTIVE'])
print(State['ACTIVE'].value)
print(State.ACTIVE.value)
print(list(State))
print(len(State))

# age = input("What is your age? ")
# print(f"Your age is {age}")

dogs = ["Roger", 1, "Syd", True, "Quincy", 7]
print("Roger" in dogs)
print("Beau" in dogs)
print(dogs[0])
print(dogs[2])
dogs[2] = "Beau"
print(dogs[2])
print(dogs[-1])
print(dogs[2:4])
print(dogs[2:])
print(dogs[:3])
print(len(dogs))
dogs.append("Judah")
print(dogs)
dogs.extend(["Blah", 5])
print(dogs)
dogs += ["Blah2", 6]
print(dogs)
dogs.remove("Quincy")
print(dogs)
print(dogs.pop())
print(dogs)

items = dogs[:]

items.insert(2, "Test")
print(items)

items[1:1] = ["Test1", "Test2"]
print(items)

# items.sort()  # error because not all same type
# print(items)

items.sort(key=str)  # modifies items sorts by string
print(items)

print(sorted(dogs, key=str))  # does not modify list
print(dogs)

# Tuples
names = ("Roger", "Syd", "Beau")

names[0]
print(names.index("Roger"))

print(len(names))

print("Roger" in names)
print(sorted(names))
# newTuple = name + ("Tina", "Quincy") # TypeError: can only concatenate str (not "tuple") to str

# Dictionaries
dog = {"name": "Roger", "age": 8}

print(dog["name"])
print(dog['name'])

dog["name"] = "Syd"
print(dog['name'])

print(dog.get("name"))
print(dog.get("color", "brown"))
dog["color"] = "green"
print(dog.get("color", "brown"))

print(dog.pop("name"))
print(dog)
print(dog.popitem())
print("color" in dog)
print(dog.keys())
print(list(dog.keys()))
print(dog.values())
print(list(dog.values()))
print(list(dog.items()))
print(len(dog))
dog["favorite food"] = "Meat"
print(dog)

del dog["favorite food"]
print(dog)
dogCopy = dog.copy()
print(dogCopy)

# Sets

set1 = {"Roger", "Syd", "Roger"}
set2 = {"Roger", "Luna", "Syd"}

intersect = set1 & set2
print(intersect)

mod = set1 | set2
print(mod)

difference = set1 - set2
print(difference)

have1 = set1 < set2
print(have1)

have2 = set1 > set2
print(have2)

print(list(set1))
print("Roger" in set1)

# Functions


def hello():
    print("Hello!")


def hello2(name="my friend", age=0):
    print(f"Hello {name}, you are {str(age)} years old!")


print(hello())
hello()

hello2("Dave")
hello2()
hello2("Dave", 1)
hello2("Dave")
hello2("", 2)
hello2()
# hello2(, 2) # syntax error


def change(value):
    value["name"] = "Syd"


val = {"name": "beau"}
change(val)

print(val)


def hello3(name):
    if not name:
        return
    print(f'Hello {name}!')
    return name, "Beau", 8


print(hello3(False))
print(hello3("Beau"))

print(hello3("Syd"))

age = 8


def test():
    age2 = 8
    print(age)
    print(age2)


print(age)
test()

# print(age2) # error
test()


def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)


talk('I am going to buy the milk')


def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()


count()


def counter():
    count = 0

    def increment2():
        nonlocal count
        count = count + 1
        return count

    return increment2


increment2 = counter()

print(increment2())
print(increment2())
print(increment2())

# Objects

age = 8

print(age.real)
print(age.imag)
print(age.bit_length())

items = [1, 2]
items.append(3)
items.pop()
print(id(items))


# Loops

condition = True
while condition == True:
    print("The condition is True")
    condition = False

count = 0
while count <= 3:
    print("The condition is True")
    count += 1

items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)

for item in range(3):
    print(item)

items = ["beau", "Synd"]
for index, item in enumerate(items):
    print(index, item)

items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue
    print(item)

print("After the loops")
