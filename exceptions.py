# Exceptions

# try:
# 	# some lines of code
# except EOFError:
# 	# handler if end of file was reached
# except <ERROR1>:
# 	# handler <ERROR1>
# except <ERROR2>:
# 	# handler <ERROR2>
# except:
# 	# handler all other errors
# else:
# 	# no exceptions were raised, the code ran successfully
# finally:
# 	# do something in any case

try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')
finally:
    result = 1

print(result)

try:
    raise Exception('An error!')
except Exception as error:
    print(error)


class DogNotFoundException(Exception):
    print('inside')
    pass


try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')


filename = './test.txt'

try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
finally:
    file.close()

with open(filename, 'r') as file:
    content = file.read()
    print(content)
