#Python Program for Largest K digit number divisible by X


k=int(input("ENTER THE VALUE OF K :- "))

x=int(input("ENTER THE VALUE OF X :- "))


m = pow(10,k)-1

m = m - (m%x)

print("Largest ",k," digit number divisible by ",x," IS ",m)