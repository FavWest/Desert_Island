from tkinter import *
import tkinter.font as font

root=Tk()

myfont=font.Font(size=14)

def gather_coconuts():
    global food, hours
    food+=2000
    hours-=1
    food_amount['text']=food
    hours_amount['text']=hours

explore=Button(text="Explore the Island", font=myfont)
coconuts=Button(text="Gather Coconuts", font=myfont, command=gather_coconuts)
cove=Button(text="Fish in the Cove", font=myfont)
explore.pack()
coconuts.pack()
cove.pack()

spacer=Label(text="", font=myfont)
spacer.pack()

food=0
hunger=0
hours=12

food_label=Label(text="Food Supplies", font=myfont)
food_amount=Label(text=food, font=myfont)
food_label.pack()
food_amount.pack()

hours_label=Label(text="Hours Remaining", font=myfont)
hours_amount=Label(text=hours, font=myfont)
hours_label.pack()
hours_amount.pack()

hunger_label=Label(text="Hunger", font=myfont)
hunger_amount=Label(text=hunger, font=myfont)
hunger_label.pack()
hunger_amount.pack()


root.mainloop()
