s="  Hi I Am Mk 11   "
print(s);

print(s.capitalize())                   #Capaitalize

print(s.center(20,' '))                 #center

print(s.count('i',0,len(s)))            #count

s=s.encode('UTF-8','strict')            #encode

print(s)

s=s.decode('UTF-8','strict')            #decode

print(s)

print(s.endswith('11',0,len(s)))        #endswith

t='Hello\tworld'

print('UnExpanded tab o/p:- '+t)

print('Expanded tab o/p:- '+ t.expandtabs(2))       #expandtabs


print(s.find('mk',0,len(s)))              #find


print(s.index('1',0,len(s)))              #index

print(s.isalnum())                        #isalnum

print(s.isalpha())                        #isalpha

print(s.isdigit())                        #isdigit

print(s.isdecimal())                      #isdecimal

print(s.islower())                        #islower

print(s.isnumeric())                      #isnumeric

print(s.isspace())                        #isspace 

print(s.istitle())                        #istitle

print(s.isupper())                        #isupper

list1 = ['h','e','l','l', 'o']            #join
print("".join(list1)) 

list1 = ['h','e','l','l', 'o']  
print("+".join(list1)) 


print(len(s))                              #len

print ("The left aligned string is : ")    
print (s.ljust(20, '-'))                    #ljust

print(s.lower())                           #lower

print(s.lstrip(' '))                       #lstrip

a='zu'
b='Ht'
c='qa'

z='zello uhisqa is mk11'

print(z)
print(z.translate(z.maketrans(a,b,c)))    #maketrans, translate


print(max(s))                             #max

print(min(s))                             #min

print(s.replace('Hi','Hello'))            #replace

print(s.rfind('1',0,len(s)))              #rfind

print(s.rindex('1',0,len(s)))             #rindex

print (s.rjust(30, '-'))                  #rjust

print(s.rstrip(' '))                      #rstrip

print(s.split(' '))                       #split

print('IIIT\nIIT\nNIT\n'.splitlines())    #splitline

print(s.startswith("Mk"))                 #startswith

print(s.strip(' '))                       #strip

print(s.swapcase())                       #swapcase

print(s.title())                          #title

print(s.upper())                          #upper

print(s.zfill(25))                        #zfill


