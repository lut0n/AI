from tkinter import *
lis = []
state = ''
weight = [0, 0, 0, 0, 0, 0, 0, 0, 0]
out = 0
x=0
y=0
while True:
        def destr():
            root.destroy()
        for i in range(9):
        	lis.append(int(input()))
        for i in range(0,9):
        	out += lis[i] * weight[i]
        if out > 0:
        	print('Square')
        else:
        	print('Line')
        root = Tk()
        c = Canvas(root, width=600, height=600)
        c.pack()
        for i in range(0,3):
                if lis[i] == 1:
                        c.create_rectangle(x,y,x+200,y+200,fill='white',outline='black')
                if lis[i] == 0:
                        c.create_rectangle(x,y,x+200,y+200,fill='black',outline='white')
                x += 200
        y += 200
        x = 0
        for i in range(3,6):
                if lis[i] == 1:
                        c.create_rectangle(x,y,x+200,y+200,fill='white',outline='black')
                if lis[i] == 0:
                        c.create_rectangle(x,y,x+200,y+200,fill='black',outline='white')
                x += 200
        y += 200
        x =0
        for i in range(6,9):
                if lis[i] == 1:
                        c.create_rectangle(x,y,x+200,y+200,fill='white',outline='black')
                if lis[i] == 0:
                        c.create_rectangle(x,y,x+200,y+200,fill='black',outline='white')
                x += 200
        d = Button(root, text='Destroy',command=destr)
        d.pack()
        root.mainloop()
        state = input()
        if state == 'w+':
                for i in range(0,9):
                        if lis[i] == 1:
                                weight[i] += 1
        if state == 'w-':
                for i in range(0,9):
                        if lis[i] == 1:
                                weight[i] -= 1
        x=0
        y=0
        lis = []
        out = 0
        print(weight)
