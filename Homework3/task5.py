list1 = [1, 2, 4, 3, 4, 5, 5]

list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        list2.remove(i)

print(list2)