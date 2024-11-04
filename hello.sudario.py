from tkinter  import *

def buttonPushed():
     print(" Button Pushed!");
    
root=Tk()
w =Label ( root, text = "Hello World!" )
w.pack()
myButton = Button(root, text="Exit", commamd=buttonPushed)
myBUtton.pack()

root.mainloop()
