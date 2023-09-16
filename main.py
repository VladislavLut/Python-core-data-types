try:
    a = int(input("Введіть число: "))
    b = int(input("Введіть число: "))
    e = int(input("Введіть число:"))
    x1 = a+b+e
    x = a*b*e
    print(x1)
    print(x)
except Exception as ex:
    print(ex)