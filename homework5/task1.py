from random import randint


# 1.1 Напишите генератор который отдает любые строки рандомным образом. (Механизм рандомайзера придумать самим)

def randomString():
    str_list = [
        "A Generator in Python is a function that returns an iterator using the Yield keyword.",
        "In this article, we will discuss how the generator function works in Python.",
        "If the body of a def contains yield, the function automatically becomes a Python generator function. ",
        "In Python, generator expression is another way of writing the generator function.",
        "The generator expression in Python has the following Syntax:"
    ]
    random_index = randint(0, len(str_list) - 1)
    yield str_list[random_index]


x = randomString()

# 1.2 Написать функцию, которая все эти слова запиешт в txt файл отделяя каждое пробелом.

def writeToFile(str):
    print(str)
    with open("data.txt", "w") as file:
        file.write(str)

writeToFile(next(x))