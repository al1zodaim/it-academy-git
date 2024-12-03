N = input("Введите количество школьников: ")

languages = {}

for student in range(1, int(N) + 1):
    M = input(f"Введите количество языков {student} - го школьника: ")
    
    for _ in range(int(M)):
        language = input()
        if languages.get(language) == None:
            languages[language] = 1
        else:
            languages[language] = languages[language] + 1


print()

all_knows_counter = 0
all_knows_languages = []

only_one_counter = 0
only_one_languages = []

for key, value in languages.items():
    if value == int(N):
        all_knows_counter = all_knows_counter + 1
        all_knows_languages.append(key)
    elif value >= 1:
        only_one_counter = only_one_counter + 1
        only_one_languages.append(key)


print(f"Количество языков, которые знают все школьники: {all_knows_counter}")
for language in all_knows_languages:
    print(language)

print(f"Количество языков, которые знает хотя бы один школьник: {only_one_counter}")
for language in only_one_languages:
    print(language)
