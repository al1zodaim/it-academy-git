def strToArray(str):

    digits = []
    for number in str:
        digits.append(int(number))

    return digits


n = input("Введите число: ")
digits = strToArray(n)

print(f"Вход: {digits}")

number = ""

for digit in digits:
    number = number + str(digit)



number = str(int(number) + 1)

digits = strToArray(number)

print(f"Выход: {digits}")