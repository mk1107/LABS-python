'''Write a function to compute 5/0 and use
try/except to catch the exceptions.
'''
try:
    a=5/0
    print(a)
except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ")
