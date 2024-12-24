import time

# определение функции декоратора
def argDec(**kwargs):
    def funcTime(input_func):    
        def output_func():

            start_time = time.time()
            
            input_func()  

            end_time = time.time()

            x = end_time - start_time
            if kwargs["seconds"] == True:
                print(x)            
            else:
                print(x / 60)
            
        return output_func
    return funcTime



@argDec(seconds=False)
def hello():
    time.sleep(1)
    


hello()