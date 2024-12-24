testList = [
    [],
    [[]],
    [[[[]]]],
]



def listDepth(list, depth):
    for item in list:
        if item:
            return listDepth(item, depth=depth+1)
        else:
            return depth + 1


results = []

for item in testList:
    if item:
        results.append(listDepth(item, 1))
    else:
        results.append(1)

print(max(results))