from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
     
        self.init_window()
        
    def init_window(self):

           self.master.title("AREZ")

           self.pack(fill=BOTH, expand=1)

           aButton = Button(self, text="A")

           aButton.place(x=0, y=0)


root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()
