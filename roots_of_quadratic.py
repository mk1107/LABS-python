'''
Write a program that accepts the a, b, and c factors
from the user (with the b and c factors allowed to be 0), and then
calculates and outputs as roots of quadratic equation.
'''
import cmath

a=int(input("ENTER VALUE OF a:- "))
b=int(input("ENTER VALUE OF b:- "))
c=int(input("ENTER VALUE OF c:- "))

if(a==0):
    exit (0)
else:
    d=((b*b)-(4*a*c))
    if(d==0):
        d1=float((-b+(cmath.sqrt(d)))/(2*a))
        print("ROOT IS:- ",d1)
    elif (d>0):
        d1=float((-b+(cmath.sqrt(d)))/(2*a))
        d2=float((-b-(cmath.sqrt(d)))/(2*a))
        print("ROOTS ARE:- ",d2," ",d1)
    else:
        d1=complex((-b+(cmath.sqrt(d)))/(2*a))
        d2=complex((-b-(cmath.sqrt(d)))/(2*a))
        print("ROOTS ARE:- ",d1," ",d2)
        
        
