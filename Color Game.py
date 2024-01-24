

from tkinter import *
from tkinter import messagebox
import random

time = 30
score = 0

win = Tk()
win.geometry('400x300')
win.title('color game')
win.configure(bg = 'black')
      
lst = ['green','brown','white','red','blue','purple',]

def start():
    if time == 30:
        countdown()
    color()

def color():
    global time
    global score
    if time > 0:
        ent.focus_set()
        if ent.get().lower() == lst[1].lower():
            score += 1
        ent.delete(0,END) 
        random.shuffle(lst)
        
        lbl_asl.config(fg = lst[1],text = lst[0],bg = 'black',font= 'tahoma ')
        lbl2.config(bg = 'black',text = str(score),fg = 'white')
    
def countdown():
    global time
    if time > 0 :
        time -= 1
        lbl_1.config(text = str(time),bg = 'black',fg = 'white')
        lbl_1.after(1000, countdown)
        if time == 0 :
            messagebox.showinfo('finish',f'The game is finish.\nYOUR SCORE IS: {score}  '  )
            lbl2.config(text = 0)
            lbl_asl.config(text = '',fg = 'black')

ent = Entry()
ent.place(y = 200, x = 195)

lbl =Label(win,text='insert color in English:',bg = 'black',fg = 'white')
lbl.place(x=70,y=200)

lbl_time =Label(text='TIME:',bg =  'black',fg = 'white')
lbl_time.place(y=20,x=175)
 
lbl_1 = Label()
lbl_1.place(y=20, x=220)
   
lblsc = Label(win,text='SCORE:',bg ='black',fg = 'white')
lblsc.place(x = 165,y = 50)

lbl2 = Label()
lbl2.place(y = 50,x=220)

lbl_asl = Label(win)
lbl_asl.place(x =175 , y = 150)

btn = Button(text='START',command= start)#command=timer
btn.place(y=250,x=170)

win.mainloop()





