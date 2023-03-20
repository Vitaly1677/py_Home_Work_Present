# Задача 2
a = input("Введите трехзначное число :")
if 0 < int(a) // 100 < 10:
    num = int(a[0]) + int(a[1]) + int(a[2])
    print(f"{a} -> {num}  ({a[0]} + {a[1]} + {a[2]})")
else:
    print("Введено не трехзначное число")

# Задача 4
countChildren = 3  # Число детей
minCountCrane = countChildren * 2  # Минимальное число журавликов
totalCrane = int(
    input(f"Введите число журавликов, изготовленных {countChildren} детьми: "))
if totalCrane >= minCountCrane and totalCrane % countChildren == 0:
    petyCrane = serjCrane = totalCrane // minCountCrane
    katyCrane = (petyCrane + serjCrane) * 2
    print(f"{totalCrane} -> {petyCrane} {katyCrane} {serjCrane}")
else:
    print("Число не соответствует условию задачи.")

# Задача 6
ticketNum = input("Введите номер билета из 6 цифр: ")
if 0 < int("1" + ticketNum) // 1000000 < 10:
    firstNum = int(ticketNum[0]) + int(ticketNum[1]) + int(ticketNum[2])
    secondNum = int(ticketNum[3]) + int(ticketNum[4]) + int(ticketNum[5])
    if firstNum == secondNum:
        print(f"{ticketNum} -> {firstNum} = {secondNum} yes")
    else:
        print(f"{ticketNum} -> {firstNum} = {secondNum} no")
else:
    print(f"Число {ticketNum} не корректно.")

# Задача 8
print("Введите размер шоколадки:")
n = int(input(" cторона n = "))
m = int(input(" cторона m = "))
k = int(input("Введите количество отломленных долек k = "))
if (k % n == 0 or k % m == 0) and k < n * m:
    print(f"{n} {m} {k} yes")
else:
    print(f"{n} {m} {k} no")