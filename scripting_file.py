#### Find out the maximum number out of 4
##a = int(eval(input('Enter the first value: ')))
##b = int(eval(input('Enter the second value: ')))
##c = int(eval(input('Enter the third value: ')))
##d = int(eval(input('Enter the 4th value: ')))
##
##if a>=b and a>=c and a>=d:
##    print(a,'is maximum')
##elif b>=a and b>=c and b>=d:
##    print(b,'is maximum')
##elif c>=a and c>=b and c>=d:
##    print(c,'is maximum')
##elif d>=a and d>=b and d>=c:
##    print(d,'is maximum')


#### Check out if the string/number is palindrome
##a = input('Enter anything to check for palindrome: ')
####if a == a[::-1]:
####    print('Its palindrome')
####else:
####    print('Its not palindrome')
##
##print('Palindrome') if a.strip().lower() == a.strip().lower()[::-1] else print('Not Palindrome')

##a = int(eval(input('Enter the count: ')))
##c = a
##while a>0:
##    
##    a -= 1
##    if not a%9:
##        continue
##    print('*'*a)
##else:
##    print('%'*30)
##
##b = 1
##while b<=c:
##    print('*'*b)
##    b += 1
##    if b>7:
##        break
##else:
##    print('$'*50)

## FOR LOOP
######################
##s = 'hello'
##for i in s:
##    print(i)

##a = [45,76,89]
##b = []
##for i in a:
##    b.append(i*2)     #b += [i*2]
##print(b)

##n = int(eval(input('Enter the number: ')))
##for i in range(1,11):
##    print(i*n)

##for i in range(1,6):
##    print(str(i)*i)


##for i in range(1,6):
##    for j in range(1,i+1):
##        print(j,end='')
##    print(end='\n')


##while 5:
##    print('wow wow...!!!!')
##    if input():
##        break


## Reverse the individual word of a statement
##s = input('Enter the statement: ')
##words = s.split()
##print(words)
##another_list = []
##for word in words:
##    another_list.append(word[::-1])
##print(another_list)
##
##rev_str = ' '.join(another_list)
##print(rev_str)

##words = s.split()
##rev_str = ''
##for word in words:
##    rev_str += word[::-1]+ ' '
##rev_str = rev_str.strip()
##print(rev_str)


## Print all the even length words from a string
##s = input('Enter the statement: ')
##for word in s.split():
##    if not len(word)%2:
##        print(word)

## Find out the second largest number from a list
##a = [45,34,78,65,99]
####a.sort()

####print('Second Largest is',a[-2])
##a.remove(max(a))
##print('Second Largest is',max(a))


### Comprehensions
## List

# Double the elements of a list
##a = [5,6,465,67,86,4,6,89]
##b = [i*2 for i in a]
##print(b)

# Double the value of list if they are even otherwise divide by 2
##c = [i/2 if i%2 else i*2 for i in a]

# find even numbers from a list
##d = [i for i in a if not i%2]
##print(d)


#### TASK for Home
## Create a python program
# firstly ask user to register
#    that should be asking for
#       username
#       fullname
#       password - password must contain at least 1 Capital, 1 small alphabet, and 1 number  with a ength of 8
# then ask for login
#       username and password
# if correct login
#   then serve with three options
#       1. Basic Calculator (+,-,*,/)
#            a = first
#            b = second
#            c = operator
#       2. Table Generator
#           2 4 6 8 10 12 14 16 18 20
#       3. Pattern Generator
#           1
#           12
#           123

####  Task for Home
## find the occurrence of each character in a string
# then check out, if all the characters are repeated for same no. of time,
# or at max, only one character is having one extra value
# then you should call it, "MY STRING"
# otherwise "NOT MY STRING"
































