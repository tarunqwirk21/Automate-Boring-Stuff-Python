def func(a):
    try:
        return 42 / a
    except ZeroDivisionError:
        print('Error!!! Cannot divide by zero')

print(func(2))
print(func(0))
print(func(42))
