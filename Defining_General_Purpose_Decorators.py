def general_purpose_decorators(func):
    def wrapper(*args,**kwargs):
        print("Position based arguments  : ",args)
        print("Keyword based arguments  : ",kwargs)
        func(*args,**kwargs)
    return wrapper

@general_purpose_decorators
def function():
    print("No arguments")

@general_purpose_decorators
def general_purpose_function(a,b,c,d=400):
    print(a,b,c,d)

general_purpose_function(1,20,300,d=4000)


    

