'''Write a program that accepts a sentence and
calculate the number of letters and digits.'''

s=input("ENTER ANY STRING:- ")
a=0
b=0
for i in s:
    if(i.isalpha()):
        a+=1
    if(i.isdigit()):
        b+=1

print("LETTERS:- ",b)
print("DIGITS:- ",a )


