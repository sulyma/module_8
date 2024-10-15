def add_everything_up(a, b):
    try:
        c = a + b
        if isinstance(c, float):
            return round(c, 3)
        else:
            return c

    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
