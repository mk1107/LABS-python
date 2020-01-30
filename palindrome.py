#Ask the user for a string and print out whether this string is a palindrome or not.

s=input("ENTER ANY STRING:- ")
x=len(s)
f=True
for i in range (0,int(x/2)-1):
    if(s[i]!=s[x-1-i]):
        f=False
        break

if(f==True):
    print("GIVEN STRING IS PALINDROME")
else:
    print("GIVEN STRING IS NOT A PALINDROME")