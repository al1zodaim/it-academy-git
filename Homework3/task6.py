list1 = [0, 2, 0, 1, 0, 5, 6, 0, -1, -2, 0]

null_count = 0

for i in list1:
    if i == 0:
        null_count = null_count + 1
        list1.remove(i)

null_list = [0 for _ in range(0, null_count)]
list1 = list1 + null_list
print(list1)