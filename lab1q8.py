'''Generate a random number between 1 and 9
(including 1 and 9). Ask the user to guess the
number, then tell them whether they guessed
too low, too high, or exactly right.'''

import random
a=(random.choice([1,2,3,4,5,6,7,8,9]))

b=int(input("ENTER ANY No. BETWEEN 0-9:- "))

if(a>b):
    print("TOO LOW")
elif(a<b):
    print("TOO HIGH")
else:
    print("EXACTLY RIGHT")


