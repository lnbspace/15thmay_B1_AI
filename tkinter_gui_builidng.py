import tkinter as tk
import sqlite3
db = sqlite3.connect('mydb.sqlite')
app = tk.Tk()
app.title('Basic Calculator')
app.geometry('300x400')

val = tk.Variable(app)
display = tk.Label(app,width=30, height=4, bg='#fff', textvariable=val);
display.pack()

count = 0
calculated = False

def calculate():
    global count
    global calculated
    global db
    calculated = True
    count += 1
    expression = val.get()
    result = float(eval(expression))
    db.execute('insert into calc_history (id, expression, result) values ({},"{}",{})'.format(count,expression,result))
    db.commit()    
    val.set(str(eval(expression)))    

def typing(v):
    global calculated
    val.set(val.get()+v)
##    if calculated:
##        calculated = False
##        val.set(v)
##    else:
##        val.set(val.get()+v)

def clear():
    val.set('')
    
tk.Button(app,text='7',width=4, height = 2,command=lambda:typing('7')).place(x=50,y=100)
tk.Button(app,text='8',width=4, height = 2,command=lambda:typing('8')).place(x=100,y=100)
tk.Button(app,text='9',width=4, height = 2,command=lambda:typing('9')).place(x=150,y=100)
tk.Button(app,text='+',width=4, height = 2,command=lambda:typing('+')).place(x=200,y=100)
tk.Button(app,text='4',width=4, height = 2,command=lambda:typing('4')).place(x=50,y=150)
tk.Button(app,text='5',width=4, height = 2,command=lambda:typing('5')).place(x=100,y=150)
tk.Button(app,text='6',width=4, height = 2,command=lambda:typing('6')).place(x=150,y=150)
tk.Button(app,text='-',width=4, height = 2,command=lambda:typing('-')).place(x=200,y=150)
tk.Button(app,text='1',width=4, height = 2,command=lambda:typing('1')).place(x=50,y=200)
tk.Button(app,text='2',width=4, height = 2,command=lambda:typing('2')).place(x=100,y=200)
tk.Button(app,text='3',width=4, height = 2,command=lambda:typing('3')).place(x=150,y=200)
tk.Button(app,text='x',width=4, height = 2,command=lambda:typing('*')).place(x=200,y=200)
tk.Button(app,text='CE',width=4, height = 2,command=clear).place(x=50,y=250)
tk.Button(app,text='0',width=4, height = 2,command=lambda:typing('0')).place(x=100,y=250)
tk.Button(app,text='=',width=4, height = 2,command=calculate).place(x=150,y=250)
tk.Button(app,text='/',width=4, height = 2,command=lambda:typing('/')).place(x=200,y=250)


app.mainloop()











##import tkinter as tk
##
##app = tk.Tk()
##app.title('My App')
##app.geometry('400x400')
##
##val = tk.Variable(app)
##count = 0
##a = tk.Label(app, text='This is a Label')
###a.pack()
###a.grid(row=0, column=1)
##a.place(x=30, y=20)
##
##b = tk.Label(app, text='It is something else')
###b.pack()
###b.grid(row=1, column=1)
##b.place(x=30, y=50)
##
##def behave():
##    #print('Hi')
##    val.set(val.get()+str(count))    
##    a.configure(text='It got changed')
##
##def behave2():
##    #print('Hi')
##    global count
##    count += 1
##    t = e.get()
##    a.configure(text=t)
##
##e = tk.Entry(app, textvariable = val)
##e.pack(side = tk.BOTTOM)
###e.grid(row=3, column=1)
###e.place(x=40, y=80)
##
##button1 = tk.Button(app, text='Click Me',width=10, bg='#fe33aa',fg='blue',command = behave)
##button1.pack(side = tk.LEFT)
###button1.grid(row=4, column=0)
###button1.place(x=30, y=120)
##
##button2 = tk.Button(app, text='Click Me As Well', command = behave2)
##button2.pack(side = tk.RIGHT)
###button2.grid(row=4, column=1)
###button2.place(x=100, y=120)
##
##
##
##
### geometry mgmt
### 1. pack(...)   BOTTOM, TOP, LEFT, RIGHT, CENTER
### 2. grid(row=r, col=c)
### 3. place(x=.., y=...)
##
##
##
##
##app.mainloop()

