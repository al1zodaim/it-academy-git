def twoSum(numbers, target):

    number_to_index = {}

    for index, number in enumerate(numbers):
     
        complement = target - number

        if complement in number_to_index:
            return [number_to_index[complement], index]
        

        number_to_index[number] = index
    
    return []

print(twoSum([2, 7, 11, 15], 9))  
print(twoSum([3, 2, 4], 6))       
print(twoSum([3, 3], 6))      