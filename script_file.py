##################################################
# Creating an Empty Class
##################################################
##class Abc():
##    pass

##################################################
# Creating Some Attributes and Methods
##################################################
##class Abc():
##    a = 10
##    print(a)
##
##    def show():
##        print('Its showtime')
##    show()

##class Abc():
##    a = 10
##    def show(self):
##        print('Its showtime')
##    def values(jyotsna):
##        print(jyotsna.a)
##        jyotsna.show()
    
##class Xyz():
##    a = 0
##    b = 0
##    c = 1
##    def change(self, m=0, n=0):        
##        self.a = m * Xyz.c
##        self.b = n / Xyz.c
##    def show(self):
##        print(self.a,self.b)
    
##class Xyz():
##    a = 0
##    b = 0
##    c = 1
##    def change(self, m=0, n=0):        
##        self.a = m * Xyz.c
##        self.b = n / Xyz.c
##    def show(self):
##        print(self.a,self.b)
##    def __init__(self):
##        print('Yes you are created')
##    def __del__(self):
##        print('You\'re gone')

##class Xyz():
##    c = 1
##    def change(self, m=0, n=0):        
##        self.a = m * Xyz.c
##        self.b = n / Xyz.c
##    def show(self):
##        print(self.a,self.b)
##    def __init__(self, i=0,j=0):
##        self.a = i
##        self.b = j
##    def __del__(self):
##        print('You\'re gone')


class Register():
    id_var = {'DevOps':0,'IoT':0,'AI':0,'ML':0}
    def __init__(self, name, course):
        self.name = name
        self.course = course
        for i in Register.id_var.keys():
            if course == i:
                Register.id_var[i] += 1
                self.my_id = i[0]+str(Register.id_var[i])
    def show(self):
        print('ID:{}'.format(self.my_id))
        print('NAME:{}'.format(self.name))
        print('COURSE:{}'.format(self.course))
    
##'''
##DevOps
##IoT
##AI
##ML
##'''
##
### Example1
##entry1 = Register('Aman','DevOps')
##entry1.show()
##
### expected output
##ID: D1
##Name: Aman
##Course: DevOps
##
########################################
### Example2
##entry2 = Register('Rehan','IoT')
##entry2.show()
##
### expected output
##ID: I1
##Name: Rehan
##Course: IoT
##
########################################
### Example3
##entry3 = Register('Thabasum','IoT')
##entry3.show()
##
### expected output
##ID: I2
##Name: Thabasum
##Course: IoT













