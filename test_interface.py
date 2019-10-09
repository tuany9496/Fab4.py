from tkinter import *

window = Tk()

window.geometry('400x400')
window.title("LA Travel")

lb1 = Label(window, text="LA | Travel like a local", font= (50))
lb2 = Label(window, text="WHERE :")
txt = Entry(window,width=10)

lb3 = Label(window, text="WHEN :")
txt2 = Entry(window,width=10)
lb6 = Label(window, text=" to ")
txt5 = Entry(window,width=10)

lb4 = Label(window, text="HOW :")
txt3 = Entry(window,width=10)
lb5 = Label(window, text="WHAT :")
txt4 = Entry(window,width=10)

lb1.grid(column=0, row=0)

lb2.grid(column=0, row=1)
txt.grid(column=1, row=1)

lb3.grid(column=0, row=2)
txt2.grid(column=1, row=2)
lb6.grid(column=2, row=2)
txt5.grid(column=3, row=2)

lb4.grid(column=0, row=3)
txt3.grid(column=1, row=3)

lb5.grid(column=0, row=4)
txt4.grid(column=1, row=4)



btn = Button(window, text="Go", bg="blue", fg="white" )

btn.grid(column=1, row=5)

window.mainloop()
