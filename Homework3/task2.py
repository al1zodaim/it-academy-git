from copy import deepcopy

text = 'abacadbbbcbd'
list1 = [text[i] + text[i + 1] for i in range(0, len(text) - 1, 2)]

print("list1: ", list1)
print("list1: ", list1[0:len(list1):2])

list2 = [ str(i) + 'a' for i in range(1, 5)]
print("list2:", list2)

del list2[1]
print("list2:", list2)

list3 = deepcopy(list2)

list3.append('2a')

print("list3: ", list3)
print("list2: ", list2)
