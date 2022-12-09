
def split_string(func):
    def wrapper():
        result = func()
        return result.split("-")
    return wrapper

def toUpper(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@split_string
@toUpper
def get_input():
    string_input = input("Enter your first name and last name separated by hyphen(-) : ")
    return string_input

print(get_input())