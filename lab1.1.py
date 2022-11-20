a = int(input('Введите числом одну сторону катета:'))
b = int(input('Введите числом вторую сторону катета:'))
с = (a*a + b*b)**0.5
print(с)

a = int(input('Введите неотрицательное число:'))
с = a//10%10
print(с)

a = int(input("Введите натуральное число: "))
print(a+2-(a%2))

a = int(input('Введите количество уроков: '))
a = a * 45 + (a // 2) * 5 + ((a + 1) // 2 - 1) * 15
print(a // 60 + 9, a % 60)

a = int(input('Введите целое число: '))
b = int(input('Введите еще одно целое число: '))
if a > b:
    print(1)
elif a < b:
    print(2)
else:
    print(0)

a = int(input('Введите целое число: '))
b = int(input('Введите еще одно целое число: '))
g = int(input('Введите еще одно целое число: '))
znach = a
if b > znach:
    znach = b
if g > znach:
    znach = g
print(znach)

x1 = int(input('Введите первую координату от 1 до 8 для вашей ладьи: '))
y1 = int(input('Введите вторую координату от 1 до 8 для вашей ладьи: '))

x2 = int(input('Введите первую координату от 1 до 8 для другой фигуры: '))
y2 = int(input('Введите вторую координату от 1 до 8 для другой фигуры: '))

if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

a = int(input("Введите первую сторону треугольника"))
b = int(input("Введите вторую сторону треугольника"))
c = int(input("Введите третью сторону треугольника"))
if a + b > c and b + c > a or a + c > b:
    print('YES')
else:
    print('NO')

a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
g = int(input("Введите третье число"))
if a == b == g:
    print("3 совпадающих числа")
elif a == b or b == g or a == g:
    print("2 совпадающих числа")
else:
    print("0 совпадающих чисел")

a = int(input())
b = int(input())
c = int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)
