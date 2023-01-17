from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady= 10)



miles = Entry(0, width=10)
miles.grid(column=1, row=0)


miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)


prime_text = Label(text="is equal to")
prime_text.grid(column=0, row=1)
prime_text.config(padx= 20, pady=20)

km = Label(text="0")
km.grid(column= 1, row= 1)
km_text = Label(text="Km")
km_text.grid(column= 2, row=1)

def convert():
    convertion = miles.get()
    new_km = int(convertion)*1.6
    km.config(text=str(new_km))

convertor = Button(text="Calculate", command=convert)

convertor.grid(column=1, row= 2)





window.mainloop()