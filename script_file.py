#############################################
# Variable Scope
#############################################
##def abc():
##    x = 20
##    print(x)
##
##abc()
##print(x)

##x = 30
##
##def abc2():
##    print(x)
##
##abc2()
##print(x)

##x = 30
##
##def abc2():
##    x = 5
##    print(x)
##
##abc2()
##print(x)

##x = 30
##def abc2():
##    global x
##    x = 5
##    print(x)
##
##print(x)
##abc2()
##print(x)

##def abc():
##    x = 10
##    def xyz():
##        x = 5
##        print(x)
##    xyz()
##    print(x)
##abc()

##def abc():
##    x = 10
##    def xyz():
##        y = 5
##        print(x,y)
##    xyz()
##    print(x)
##abc()

##def abc():
##    x = 10
##    def xyz():
##        nonlocal x
##        x = 5
##        print(x)
##    print(x)
##    xyz()
##    print(x)
##abc()

##y = 20
##def abc():
##    x = 10
##    def xyz():
##        nonlocal x
##        global y
##        y = 40
##        x = 5
##        print(x, y)        
##    print(x)
##    xyz()
##    print(x)
##
##print(y)
##abc()
##print(y)


##################################################
### Generate Comprehension
##################################################
##a = [4,5,4,46,84,7,3,5,89]
##print(a)
##b = [i for i in a if not i%2]
##print(b)
##c = (i for i in a if not i%2)
##print(c)

##################################################
# Function Decorator
##################################################

##def decorate(f):
##    def another():
##        print('I am decorating you')
##        f()
##        print('You are decorated  now')
##    return another
##
##def simple():
##    print('I am simple')
##
##simple()
##
##print('-'*20)
##print()
##simple = decorate(simple)
##simple()


###### Do practice this
##def decorate(f):
##    def another():
##        print('I am decorating you')
##        f()
##        print('You are decorated  now')
##    return another
##
##@decorate
##def simple():
##    print('I am simple')
##
##simple()


##def decorate(f):
##    def another():
##        print('I am decorating you')
##        f()
##        print('You are decorated  now')
##    return another
##
##@decorate
##@decorate
##def simple():
##    print('I am simple')
##
##
##simple()

### Bringing Module into file
##import module1
##module1.abc()


### creating alias for the modules
##import module1 as m
##m.abc()

### Using from-import
##from module1 import abc
##abc()

##from module1 import abc, data
##print(data)
##abc()

##from module1 import abc as a, data as d
##print(d)
##a()

##from module1 import *
##abc()
##print(data)
##print(values)
##print(doubler(4))



########################################################
# File Handling
########################################################

##f = open('myfile.txt') # 'r'
##content = f.read()
##f.close()

##f = open('myfile.txt','w')
##f.write('This is new content')
##f.close()
##
##f = open('myfile.txt') # 'r'
##content = f.read()
##f.close()
##print(content)


##f = open('myfile.txt','a')
##f.write('This is one content')
##f.close()
##
##f = open('myfile.txt','a')
##f.write('\nThis is one more content\n')
##f.close()

##f = open('myfile.txt') # 'r'
##content = f.read()
##f.close()
##print(content)






