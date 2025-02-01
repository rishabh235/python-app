#decorator

def logger(func):   
    def wrapper():
        print(f"Someonce called {func.__name__}")
        func()
        print(f"{func.__name__} is executed successfully")
    return wrapper

@logger
def processData():
    print("connecting to DB")
    print("data processed")

processData()