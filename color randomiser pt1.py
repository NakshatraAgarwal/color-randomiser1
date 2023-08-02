from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.config(bg="cyan")

label = Label(root,font=("times",30),bg="white")
label.place(relx=0.5,rely=0.5,anchor=CENTER)

class game():
    def __init__(self):
        self.__score = 0
        
    def update(self):
        self.text = ["white","black","yellow","red"]
        self.random_no = random.randint(0,3)
        self.color = ["white","black","yellow","red"]
        self.random_color = random.randint(0,3)
        label["text"] = self.text[self.random_no]
        label["fg"] = self.color[self.random_color]
        

obj = game()

btn = Button(root,text="start",command=obj.update)
btn.pack()
root.mainloop()
        
        
        
    