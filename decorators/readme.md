# Decorators

In Python, decorators are a powerful feature that allows you to modify or 
enhance the behavior of functions, methods, classes, or even modules without 
directly modifying their source code. Decorators provide a way to wrap or 
decorate the original object with additional functionality. 

In Python, decorators are implemented using the "@" symbol followed by the 
name of the decorator function, which is placed on the line directly above 
the object being decorated. The decorator function takes the object being 
decorated as an argument and typically returns a new object that replaces the 
original. 

Here's a simple example to illustrate the basic syntax and usage of 
decorators:

```python
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def my_function():
    print("Inside my_function")

# Calling the decorated function
my_function()
```

In the example above, `my_decorator` is a decorator function that takes 
`my_function` as an argument. It defines an inner function called `wrapper`, 
which adds some additional functionality before and after the original 
function `my_function` is called. The `wrapper` function is returned and replaces 
the original function. 

When my_function is called, it is actually calling the `wrapper` function 
returned by the decorator. The output of running the code will be:

```bash
Before function execution
Inside my_function
After function execution
```

This demonstrates how the decorator modifies the behavior of `my_function` by 
adding the print statements before and after its execution. 

Decorators are commonly used for various purposes in Python, such as logging, 
timing, authentication, memoization, and more. They provide a clean and 
reusable way to add functionality to existing code without modifying it 
directly. 

It's important to note that decorators can also take arguments and be chained 
together to apply multiple decorators to a single object. Additionally, there 
are built-in decorators in Python, such as `@property` and `@staticmethod`, which 
have specific purposes and usage patterns. 

Overall, decorators are a powerful and flexible feature in Python that enable 
you to enhance and modify the behavior of objects in a concise and elegant 
manner. 

