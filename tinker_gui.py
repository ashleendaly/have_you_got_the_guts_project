from tkinter import *
from urllib.request import urlopen
from country_list import countries_for_language
from newsweather import news, weather

countries = []
for i in range(len(countries_for_language('en'))):
    countries += [countries_for_language('en')[i][1]]

colleagues = {}


# Adds colleague to list
def add_colleague_to_dict():

    global country_entry
    global name_entry
    global city_entry



    confirmation_label.config(text=f"{name_entry.get()} has been added")

    root.update()


# removes colleague from list
def remove_colleague_to_list():
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

# ------- LEFT FRAME ----------
# ---- Add Colleague
add_colleague_label = Label(left_frame, text="Add Colleague").grid(row=0, column=0, padx=5, pady=5, columnspan=2)

# - Name Label and Entry
name_label = Label(left_frame, text="Name:")
name_label.grid(row=1, column=0, padx=5, pady=5)

name_entry = Entry(left_frame)
name_entry.grid(row=1, column=1, padx=5, pady=5)

# - Country Label and Entry
country_label = Label(left_frame, text="Country:")
country_label.grid(row=2, column=0, padx=5, pady=5)

country_entry = Entry(left_frame)
country_entry.grid(row=2, column=1, padx=5, pady=5)

# - City Label and Entry
city_label = Label(left_frame, text="City:")
city_label.grid(row=3, column=0, padx=5, pady=5)

city_entry = Entry(left_frame)
city_entry.grid(row=3, column=1, padx=5, pady=5)

# - Add Colleague Button
add_colleague_button = Button(left_frame, text="Add", command=add_colleague_to_dict)
add_colleague_button.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

# - Confirmation Label
confirmation_label = Label(left_frame, text="")
confirmation_label.grid(row=5, column=0, padx=5, pady=5, columnspan=2)


# ---- Select Colleague Drop Down Menu
clicked = StringVar
colleague_drop = OptionMenu(left_frame, clicked, colleagues)
colleague_drop.grid(row=6, column=0, padx=10, pady=5, columnspan=2)

# ------- Right FRAME ----------
# ---- Display Weather


# ---- Display News




root.mainloop()