# UDFs
#####################################################
### No input params, no Returns
##def xyz():
##    print('Wow this is my function')
##    
##xyz()


### input params, no Returns
##def xyz2(a):
##    print('I got,',a)
##
##xyz2('Hiii')

### no input params, Return is there
##def xyz3():
##    print('wow')
##    return 'nice'
##    print('good')
##
##xyz3()
##k = xyz3()


### input params, return is there
##def xyz4(a):
##    print('It does something...')
##    if a<10:
##        return a*10
##    else:
##        return a/10
##m = xyz4(45)
##
##print('Value of m={}'.format(m))
##
##n = xyz4(3)
##print('Value of n={}'.format(n))


##### Return Multiple Values
##def xyz5(n):
##    return n*2, n**3, (n/2)+4
##
##a = xyz5(34)
##print(a)

#### Multiple Input Parameters
##def xyz6(a,b,c):
##    return(a+b-c)
##
##m = xyz6(4,65,3)
##print(m)

### Named Parameters
##print(xyz6(a=34,c=10,b=5))

#### Default Valued Parameters (It always goes from right to left)
##def xyz7(a,b,c=10):
##    return a+b-c
##
##def xyz8(a=0,b=20,c=10):
##    return a+b-c

#### Variable Length Arguments
##def xyz9(a, *b):
##    print(b)
##    print(a)
##
##def xyz10(*a):
##    for i in a:
##        print(i)
##
##def xyz11(m=10,n=20,*a):
##    k = 0
##    for i in a:
##        k += i
##    return (m-n)*k

#### Variable Length Keyword arguments
##def xyz12(**a):
##    for i in a:
##        print(i,a[i])
##    print(a)
##
##def xyz13(*args, **kwargs):
##    print(args)
##    print(kwargs)

######################################################

##z = '''
##a = 10
##b = 30
##print(a+b)
##'''
##print('go')

##def abc():
##    '''
##    This is my function document
##    and I have created inside the function only
##    '''
##    print('Hello')


#######################################################
### Assigning a function to a variable
##def abc():
##    print('Hello')
##a = abc
##a()

### Recursions
##def abc2(n):
##    if n < 10:
##        return n
##    else:
##        print(abc2(n-1))
##        return n-1
        
# Nested Functions
##def abc3(x):
##    def ab(y):
##        print(y)
##    ab(x)

##def abc4(x):
##    print('good',x)    
##    def ab(y,z):
##        print(y+z)
##    return ab(x,x*2)

##def abc5(x):
##    print('good',x)    
##    def ab(y,z):
##        return (y+z)
##    return ab(x,x*2)

##def abc6(x):
##    print('good',x)
##    def ab(y,z):
##        return y+z
##    return ab
        
#######################################################
# Annonymous Functions
## LAMBDA Expressions

# How to write
##def abc(n):
##    return n*2
##
##abc2 = lambda n:n*2

# Why do we need this?????
a = [3,54,6,8,34,7,11,44]

##def operate(k):
##    for i in k:
##        print(i*2)
##    print('-'*20)
##
##def operate2(k):
##    for i in k:
##        print(i**3)
##    print('-'*20)
##
##operate(a)
##operate2(a)

##def operation(k,f):
##    for i in k:
##        print(f(i))
##    print('-'*20)
##
##operation(a,lambda n:n*2)
##operation(a,lambda n:n**3)


##print(list(map(lambda n:n+4, a)))

##print(list(filter(lambda n:n%2==1, a)))

#######################################################
# Generator
#################
def xyz(n):
    yield n+1
    yield n+2
    for i in range(1,3):
        yield n*i





















