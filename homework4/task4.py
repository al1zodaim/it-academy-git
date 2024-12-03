numbers_list1 = set([1, 2, 3, 4, 5])
numbers_list2 = set([1, 2, 3, 4, 5, 6])

numbers_dict = {}

for number in numbers_list1:
    if numbers_dict.get(number) == None:
        numbers_dict[number] = 1


for number in numbers_list2:
    if numbers_dict.get(number) == None:
        numbers_dict[number] = 1
    else:
        numbers_dict[number] = numbers_dict[number] + 1

print(numbers_dict)

counter = 0
for value in numbers_dict.values():
    if value == 1:
        counter = counter + 1

print(counter)