def func1(func):
    call=False
    def wrapper():
        nonlocal call
      
        if not call:
            func()
            call=True
        else:
            print("function already run")
    return wrapper
@func1
def show():
    print("functio is runnung")
show()
show()