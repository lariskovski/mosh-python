# Ref: https://www.youtube.com/watch?v=FsAPt_9Bf3U
# ====================
# Function decorators example
# ====================
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'Wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function


# ====================
# Class decorators example
# ====================
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print(f'Wrapper executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)
        


# ====================
# No decorators example
# ====================
# def display():
#     print('Display function ran')
# decorated_display = decorator_function(display)
# decorated_display()


# ====================
# Decorators Example
# ====================
# This decoration equals to
# display = decorator_function(display)
@decorator_function
def display():
    print('Display function ran')
display()


@decorator_class
def display_info(name, age):
    print(f'Display info ran with arguments {name} and {age}')
display_info('larissa', '24')