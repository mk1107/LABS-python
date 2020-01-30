#FACTORIAL OF A No.


a=int(input("ENTER ANY No.:- "))
fact=1
for i in range(1,a+1):
    fact*=i


print("FACTORIAL OF ",a," IS ",fact)
