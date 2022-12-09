
def decorator_func(val1,val2):
    def inner_func(func):
        def wrapper(*args,**kwargs):
            print("Sum = ",val1+val2)
            result = func(*args,**kwargs)
            return result
        return wrapper
    return inner_func

@decorator_func(2,3)
def string_merge(*args,**kwargs):
    string_out = ""
    for x in args:
        string_out = string_out + " " + x
    return string_out

print(string_merge("Gawsik","Kumaran","GK"))

