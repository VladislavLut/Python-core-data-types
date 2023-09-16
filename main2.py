try:
    a = int(input('Довжина ромба: '))
    b = int(input('Ширина ромба: '))

    x = (a + b) * 2

    print(x)

except Exception as ex:
    print(ex)