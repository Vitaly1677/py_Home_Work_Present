# Задача 10
numberСoins = int(input("Введите кол-во монеток = "))
countHeads = 0
countTails = 0
print("Введите стороны монет - РЕШКА введите 1 или 0 если ОРЕЛ:")
for i in range(numberСoins):
    coinSide = int(input(f"Монета {i+1} из {numberСoins} = "))
    if coinSide == 0:
        countHeads += 1
    elif coinSide == 1:
        countTails += 1
    else:
        print("Не верно введено значение. Программа прервана.")
        break
else:
    if countTails > countHeads:
        print(countHeads)
    else:
        print(countTails)

# Задача 12
s = int(input("Введите сумму чисел S (<= 2000) : "))
p = int(input("Введите произведение чисел P : "))
flagExit = False
if 0 < s <= 2000 and p > 0:
    for x in range(s):
        if flagExit :
            break
        for y in range(p):
            if s == x + y and p == x * y:
                print(f"{s} {p} -> {x} {y}")
                flagExit = True
                break
    else:
        print("Сумма и произведение расчитанны не верно.")
else:
    print("Чесла не натуральные или превышено ограничение.")

# Задача 14
n = int(input("Введите число N: "))
i = 0
resultStr = str(n) + " - > "
while 2 ** i <= n:
    resultStr += str(2**i) + " "
    i += 1
print(resultStr)