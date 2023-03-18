def gg(func):
    def wrap_func():
        print("code before func")

        func()

        print("code after func")

    return wrap_func
@gg
def func_needs_decorator():
    print("This function is in need of a decorator")
    print("This function is in need of a decorator")
    print("This function is in need of a decorator")

func_needs_decorator()
