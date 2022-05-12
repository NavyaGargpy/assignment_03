#Ques_02..............


# the following commands can be used:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ** for exponential

number_1 = int(input('Enter first number: '))
operation = input() 
number_2 = int(input('Enter second number: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

elif operation == '**':
    print('{} ** {} = ' .format(number_1, number_2))
    print(number_1**number_2)

else:
    print('You have not typed a valid operator, please run the program again.')