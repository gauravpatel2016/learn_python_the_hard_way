def is_print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def _print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin.")

is_print_two("Zed","Shaw") 
_print_two_again("Zed","Shaw") 
print_one("First!") 
print_none()