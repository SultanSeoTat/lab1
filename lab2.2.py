# 1 задача
a, b = map(int, input().split())

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=' ')

# 2 задача
def test(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n
a = int(input('Введите число: '))
print(test(a))

# 3 задача
x = int(input('Введите число '))
for i in range(1,x+1):
    if x % i == 0:
      print(i,end = ' ')

# 4 задача
a = int(input('Введите число '))
print('Сумма чисел от 1 до', a, '=', sum([i for i in range(1, a+1)]))

# 5 задача
a = input()
b = 0
for index, val in enumerate(a):
    b += (int(val) * 2 **(len(a) - index - 1))
print(b)

#6 задача
def power(a:float, b:int):
    return a**b

a = input().split()
print(power(float(a[0]), int(a[1])))

# 7 задача
def election(x:int, y:int, z:int):
   summ = sum((x, y, z))
   if summ > 3 or summ < 0:
       return None
   if summ > 1:
       return 1
   else:
       return 0
a = input().split()
print(election(int(a[0]),int(a[1]), int(a[2])))

# 8 задача
cur_sum = 0.0

def add_to_bank_account(summ: float):
    global cur_sum
    cur_sum += summ

def take_from_bank_account(summ: float):
    global cur_sum
    cur_sum -= summ

def money_conv(summ: float, before, after):
    match before, after:
        case 'USD' as before, 'KZT' as after:
            return summ*470
        case 'KZT' as before, 'USD' as after:
            return summ / 470