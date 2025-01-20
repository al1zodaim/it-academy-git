numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}

s = input('Вход: ')

index = 0
result = 0

while index < len(s) - 1:

    number = numbers.get(s[index] + s[index + 1])
    if number != None:
        result = result + number
        index = index + 2
    else:
        result = result + numbers.get(s[index])
        index = index + 1
        if index == len(s) - 1:
            result = result + numbers.get(s[index])

            
print(result)
