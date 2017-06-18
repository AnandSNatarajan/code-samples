
#Ways of passing argument to a function : same position or different positions with qualifier
print("\nExample: Function Arguments")
def greet_user(msg, name):
    print(msg + " " + name)
greet_user("Good Morning", "Anand")
greet_user(name="Anand", msg = "Good Morning")

# Variable arguments to a function
def greet_user(msg, *names):
    print(msg)
    for name in names:
        print(name)
greet_user("Good Morning", "Anand", "Chump")

# Closure : Outer function returns an inner function
# In below example, the arguments to outer function are used to create an inner function
# operation (printing) and different new functions can be derived by passing different
# arguments to outer function.
# This can be used for avoiding defining global variables
print("\nExample : Closure")
def outer_func(value):
    def inner_func():
        print(value)
    return inner_func

new_inner_func = outer_func(10)
new_inner_func()

# Even same name can be used since the scope of inner_func is inside outer_func
inner_func = outer_func(10)
inner_func()

print("\nExample : Closure contents")
print(new_inner_func.__closure__)
print(new_inner_func.__closure__[0].cell_contents)

#Decorator
print("\nExample : Decorator")
def orig_func(value):
    print("Value is", value)

def decorator_func(orig_func):
    def decorated_func(*args, **kwargs):
        print("I am decorated")
        orig_func(*args, **kwargs)
    return decorated_func

orig_func(20)
orig_func = decorator_func(orig_func)
orig_func(10)

# Using the @symbol can decorate a function using the decorator function specified
print("\nExample : Optimized Decorator")
@decorator_func
def orig_func2(value):
    print("Value is", value)

orig_func2(15)

#Multiple decorators can be chained
print("\nExample : Multiple Decorator")
@decorator_func
@decorator_func
def orig_func2(value):
    print("Value is", value)

orig_func2(15)
