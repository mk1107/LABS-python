'''Create a program that asks the user to enter
their name and their age. Print out a message
addressed to them that tells them the year that
they will turn 100 years old.
'''

name=input("ENTER YOUR NAME: ")
age=int(input("ENTER YOUR AGE: "))

a=2019+(100-age)

b=name+" WILL TURN 100 ON "

print(b,a)