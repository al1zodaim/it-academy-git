list1 = ['a', 'b', 'c']
list1_tuple = tuple(list1)
print(list1)
print(list1_tuple)
print()


tuple1 = ('a', 'b', 'c')
tuple1_list = list(tuple1)

print(tuple1)
print(tuple1_list)
print()

a, b, c = ('a', 2, 'python')
print(a)
print(b)
print(c)
print()

tuple2 = ("1, 2, 3", )
for i in tuple2:
    print(i)

print(len(tuple2))