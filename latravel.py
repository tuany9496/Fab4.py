import tkinter as tk
from tkinter import *
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class MainPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       # label = tk.Label(self, text="This is page 1")
       # label.pack(side="top", fill="both", expand=True)

       # Title
       lb1 = Label(self, text="LA | Travel like a local", font= (50))
       lb1.grid(column=0, row=0)

       # Where
       lb2 = Label(self, text="WHERE :")
       lb2.grid(column=0, row=1)
       self.txt_where = Entry(self,width=10)
       self.txt_where.grid(column=1, row=1)

       # When
       lb3 = Label(self, text="WHEN :")
       lb3.grid(column=0, row=2)
       self.txt_when_from = Entry(self,width=10)
       self.txt_when_from.grid(column=1, row=2)
       lb6 = Label(self, text=" to ")
       lb6.grid(column=2, row=2)
       self.txt_when_to = Entry(self,width=10)
       self.txt_when_to.grid(column=3, row=2)

       # How
       lb4 = Label(self, text="HOW :")
       lb4.grid(column=0, row=3)
       self.txt_how = Entry(self,width=10)
       self.txt_how.grid(column=1, row=3)


       # What
       lb5 = Label(self, text="WHAT :")
       lb5.grid(column=0, row=4)
       #txt4.grid(column=1, row=4)

       # What Checkbuttons
       self.checkbutton_eat = Checkbutton(self, text = 'Resturants')
       self.checkbutton_eat.grid(column=1, row= 4)
       self.checkbutton_eat.deselect()
       # Set Checkbutton_eat value
       self.eat = StringVar()
       self.eat.set ('Dont Display')
       self.checkbutton_eat.config (variable = self.eat, onvalue = 'Display', offvalue = 'Dont Display' )

       self.checkbutton_hotel = Checkbutton(self, text = 'Hotels')
       self.checkbutton_hotel.grid(column=2, row= 4)
       self.checkbutton_hotel.deselect()

       self.checkbutton_see = Checkbutton(self, text = 'Sightseeing')
       self.checkbutton_see.grid(column=1, row= 5)
       self.checkbutton_see.deselect()
class SearchResultPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = MainPage(self)
        p2 = SearchResultPage(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Main Page", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Search", command=p2.lift)


        b1.pack(side="left")
        b2.pack(side="left")


        p1.show()

if __name__ == "__main__":
    self = tk.Tk()
    main = MainView(self)
    main.pack(side="top", fill="both", expand=True)
    self.wm_geometry("600x400")
    self.mainloop()
