def typeCheck(input_func):    
    def output_func(*args):
        isOK = True
        for item in args:
            if type(item) != int:
                print("Тип не совпадает!")
                isOK = False
                break
        
    
        if isOK:
            input_func(*args)  
        
    return output_func


@typeCheck
def add(a, b):
    print(a + b)


add(2, 3)
add(2, "f")