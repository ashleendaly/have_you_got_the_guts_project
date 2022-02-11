from tkinter import *
from urllib.request import urlopen
from newsweather import news, weather

colleagues = []


def add_colleague_to_dict(name, city):
    pass


# ---- Create Root Window
root = Tk()
root.title("Remote Colleagues' Environment")
root.maxsize(900, 600)

# ---- Create left and right frames
left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0,  padx=20, pady=5)

right_frame = Frame(root, width=650, height=400)
right_frame.grid(row=0, column=1, padx=10, pady=5)

# ---- Add Colleague
add_colleague_label = Label(left_frame, text="Add Colleague").grid(row=0, column=0, padx=5, pady=5, columnspan=2)

city_label = Label(left_frame, text="City:")
city_label.grid(row=1, column=0, padx=5, pady=5)

city_text = StringVar()
city_entry = Entry(left_frame, textvariable=city_text)
city_entry.grid(row=1, column=1, padx=5, pady=5)

name_label = Label(left_frame, text="Name:")
name_label.grid(row=2, column=0, padx=5, pady=5)

name_text = StringVar()
name_entry = Entry(left_frame, textvariable=name_text)
name_entry.grid(row=2, column=1, padx=5, pady=5)

add_colleague_button = Button(left_frame, text="Add", command=add_colleague_label)
add_colleague_button.grid(row=3, column=0, padx=5, pady=5, columnspan=2)




root.mainloop()