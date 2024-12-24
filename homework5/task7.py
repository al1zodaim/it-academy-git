def counter(func):
    
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        if wrapper.count <= 5:
            func(*args, **kwargs)
        else:
            print("Лимит превышен!!!")
    
    wrapper.count = 0
    return wrapper


# Функция, вызовы которой нужно считать
@counter
def f():
    print("Hello")


f()
f()
f()
f()
f()
f()
f()