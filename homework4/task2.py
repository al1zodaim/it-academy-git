N = input("Введите количество стран: ")

countries = {}

for _ in range(int(N)):
    country = input()
    splitted_country = country.split(' ')
    countries[splitted_country[0]] = splitted_country[1:]

print()

M = input("Введите количество запросов: ")
requests = []

for _ in range(int(M)):
    city = input()
    requests.append(city)

print()

for request in requests:
    for key, value in countries.items():
        if request in value:
            print(key)