def main_func(doc):
    def wrapper_func():
        return doc.upper()
    return wrapper_func

result = main_func("Gawsik")
print(result())