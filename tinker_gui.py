from tkinter import *
from newsweather import news, weather


def add_colleague_to_dict(name, city):
    pass


# ---- Create Root Window
root = Tk()
root.title("Remote Colleagues' Environment")
root.geometry('700x350')

# ---- Input college city and name
city_label = Label(root, text="Enter City")
city_label.pack()

city_text = StringVar()
city_entry = Entry(root, textvariable=city_text)
city_entry.pack()

colleagues = []



root.mainloop()