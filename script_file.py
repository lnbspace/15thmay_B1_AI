##class Abc():
##    def __init__(self, d):  # will do while creating object
##        self.data = d
##        print('Created')
##    def __del__(self):      # will do for del
##        print('Deleted')
##    def __str__(self):      # will do for print
##        return self.data        
##    def __repr__(self):                 # will do for the repr function or direct data
##        return 'My Data\n'+self.data
##    def __getitem__(self, ind):         # works for indexing and slicing
##        return self.data[ind]
##    def __len__ (self):                 # works for len function
##        return len(self.data)
##    def __call__(self,a=1,b=''):        # makes the object callable
##        return (self.data * a) + b
##    def __ge__ (self, obj):                     # Operator Overloading
##        return len(self.data) >= len(str(obj))
##    def __gt__ (self, obj):                     # Operator Overloading
##        return len(self.data) > len(str(obj))
##    def __eq__ (self, obj):                     # Operator Overloading
##        return len(self.data) == len(str(obj))
##
### Task
############
### Create OO to subtract two strings
##
### Input
### s = String('aaaab')
### s2 = String('ac')
##
### s - s2
##
### Output
### aaab

##class Abc():
##    def __init__(self, data=''):
##        self.data = data
##    def show(self):
##        print(self.data)
##
##class Pqr(Abc):
##    def something(self):
##        print('Yeah it is something')
##
##class Xyz(Abc):
##    def some(self):
##        print('its from Xyz')
##
##class Mno(Pqr):
##    def my(self):
##        print('My is MNO')
##
##class Zyx():
##    __val = Abc                         # Data Hiding
##    def do(self):
##        print('I will do everything')
##
##class Rqp(Abc, Zyx):
##    def rrr(self):
##        print('Raaraaraa')
##    def do(self):                       # Method Overriding
##        print('I will do nothing')
##
##class Name(Abc):
##    def show(self):
##        Abc.show(self)
##        print('wow')


## Error and Exception Handling  
##try:
##    a = int(input('Enter the first value:'))
##    b = int(input('Enter the second value:'))
##    print(a/b)
##except ValueError:
##    print('It didn\'t work well')
##except ZeroDivisionError:    
##    print('You tried dividing by zero')
##    print(a)
##
##print('Its going on well')
##print('Its done')


#### Handles any kind of error (Exception)
##try:
##    a = int(input('Enter the first value:'))
##    b = int(input('Enter the second value:'))
##    print(a/b)
##except Exception:
##    print('It didn\'t work well')
##
##print('Its going on well')
##print('Its done')










        
