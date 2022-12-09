
def decorator_func(func):
    def wrapper(x):
        result = func(x)
        return result
    return wrapper

@decorator_func
def power_of_func(num):
    return int(num)*int(num)

num = input("Enter the number : ")
print(power_of_func(num))