from tkinter import *

'''
pip install tkintertable
no console caso aconteça o erro
'''


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self.master)
        self.msg = Label(self, text='Olá, mundo!')
        self.msg.pack()
        self.pack()
app = Application()
mainloop()
