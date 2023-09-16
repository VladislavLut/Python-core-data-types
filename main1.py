try:
    a = int(input('Зарплата за місяць: '))
    b = int(input('Місячний платіж за кредит: '))
    d = int(input('Заборгованість за комунальні платежі:'))

    x1 = a - b - d

    print(x1)
except Exception as ex:
    print(ex)