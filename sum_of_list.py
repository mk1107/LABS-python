#Take any list data type with numbers. Print Sum of all the numbers in the list.

t = 0

list = [11, 5, 17, 18, 23]  

for i in range(0, len(list)): 
    t = t + list[i] 
  
print("Sum of all elements in given list: ", t) 