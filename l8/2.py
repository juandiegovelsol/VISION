value = input('Please enter a natural number: ')

try:
    value = int(value)
    reciprocal = 1 / value
except ValueError:
    try:
        value = float(value)
        reciprocal = 1 / value
    except ValueError:
        print('This is not a natural number.')
        exit()
except ZeroDivisionError:
    print('The number cannot be zero.')
    exit()
else:
    print('The reciprocal of', value, 'is', reciprocal)