from tkinter import *
import random
r=Tk()
r.title("ROLL DICE")
r.geometry("800x600")

#label defintion
label=Label(r,font=('comics',250,'bold'),text='')

#function defintion
def RollDice():
    roll=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

    label.configure(text=random.choice(roll))  #label configuration....configuring the label created in line 8
    label.pack()

#button creation
button=Button(r,font=('comics',30,'bold'),text="Roll Dice",command=RollDice)
button.pack()


r.mainloop()
