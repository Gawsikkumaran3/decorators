#Program 1 with passing arguments

def add_num1_num2(num1):
    def wrapper(num2):
        return num1+num2
    return wrapper

num1 = input("Enter the first number to be added : ")
result = add_num1_num2(int(num1))
num2 = input("Enter the second number to be added : ")
print(result(int(num2)))

#Program 2 with no arguments

def welcome():
    def wrapper():
        print("Hello!Good morning")
    return wrapper

greeting = welcome()
greeting()