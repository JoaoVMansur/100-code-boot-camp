from tkinter import *


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady= 20)

#Label

my_label = Label(text="I'm a label", font=("Arial", 24))
my_label.grid(column=0, row=0)
my_label["text"] = "New text"
my_label.config(text="New test")

#Button

def button_clicked():
    new_label = input.get()

    my_label.config(text=new_label)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row= 1)

new_button = Button(text="Place me")
new_button.grid(column=2, row=0)
#Entry

input = Entry(width=10)
new_label = input.get()


input.grid(column=3, row=2)






window.mainloop()