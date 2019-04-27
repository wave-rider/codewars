'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:
'''
def calculate(func, arg):
     if func is None:
        return arg
     else:
        return func(arg)

def zero(func = None): return calculate(func, 0)
def one(func = None): return calculate(func, 1)
def two(func = None):return calculate(func, 2)
def three(func = None): return calculate(func, 3)
def four(func = None): return calculate(func, 4)
def five(func = None): return calculate(func, 5)
def six(func = None): return calculate(func, 6)
def seven(func = None): return calculate(func, 7)
def eight(func = None): return calculate(func, 8)
def nine(func = None): return calculate(func, 9)

def plus(arg1): return lambda arg2: arg2 + arg1
def minus(arg1): return lambda arg2: arg2 - arg1
def times(arg1): return lambda arg2: arg2 * arg1
def divided_by(arg1): return lambda arg2: arg2 // arg1

'''
Test.describe('Basic Tests')
Test.assert_equals(seven(times(five())), 35)
Test.assert_equals(four(plus(nine())), 13)
Test.assert_equals(eight(minus(three())), 5)
Test.assert_equals(six(divided_by(two())), 3)
'''

print(seven(times(five())))
