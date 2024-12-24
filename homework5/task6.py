def outer(number):
 
    def inner(number1):
        nonlocal number
        print(number * number1)
 
    return inner

multiply = outer(5)

multiply(1)
multiply(2)
multiply(3)
multiply(4)
multiply(5)
multiply(6)
multiply(7)
multiply(8)
multiply(9)
multiply(10)