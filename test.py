def log(func):
    def wrapper(name):
        print('before calling'),func.__name__
        func(name)
        print('end calling'),func.__name__
    return wrapper
@log
def morning(name):
    print('hello',name)
if(__name__=='__main__'):
    morning('NNN')