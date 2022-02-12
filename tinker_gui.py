from tkinter import *
from urllib.request import urlopen
from newsweather import weather, news
from PIL import Image, ImageTk
#from country_list import countries_for_language

colleagues = []

# Adds colleague to list
def add_colleague_to_list():

    global country_entry
    global name_entry
    namestr = name_entry.get()
    countrystr = country_entry.get()

    colleagues.append((namestr, countrystr))

    confirmation_label.config(text=f"Details for {namestr} have been added")
    pass


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

#Load logo
Logo = Image.open("/Users/user/Desktop/have_you_got_the_guts_project/Logo.png")

#resize logo
resized = Logo.resize((300, 100), Image.ANTIALIAS)

new_Logo = ImageTk.PhotoImage(resized)

label = Label(
    root,
    image=new_Logo)
label.place(x=40, y=15)

# ---- Add Colleague
add_colleague_label = Label(left_frame, text="Add Colleague").grid(row=0, column=0, pady=5, columnspan=2)

name_label = Label(left_frame, text="Name:")
name_label.grid(row=1, column=0, pady=5)

name_entry = Entry(left_frame)
name_entry.focus_set()
name_entry.grid(row=1, column=1, pady=5)

country_label = Label(left_frame, text="Country:")
country_label.grid(row=2, column=0, pady=5)

country_entry = Entry(left_frame)
country_entry.focus_set()
country_entry.grid(row=2, column=1, padx=5, pady=5)

add_colleague_button = Button(left_frame, text="Add", command=add_colleague_to_list)
add_colleague_button.grid(row=3, column=0, pady=5, columnspan=2)


confirmation_label = Label(left_frame, text="")
confirmation_label.grid(row=4, column=0, pady=5, columnspan=2)

space = Label(left_frame, text="")
space.grid(row=5, column=0, pady=20)


# ---- Select Colleague Drop Down Menu

existing_colleague_label = Label(left_frame, text="Select Existing Colleague")
existing_colleague_label.grid(row=6, column=0, pady=5, columnspan=2)

clicked = StringVar()
colleague_drop = OptionMenu(left_frame, clicked, colleagues)
colleague_drop.grid(row=7, column=0, pady=5, columnspan=2)

# ------- Right FRAME ----------

#====Images====#
image = Label(root, bitmap="")
image.grid(row=0, column=1, pady=5, columnspan=2)

image['bitmap'] = "/Users/user/Desktop/have_you_got_the_guts_project/Earth.png"



# ---- Display Weather
# Weather in Colleagues country
def weather(country, location):
    if type(country) != str or type(city) != str or len(country)==0 or len(city)==0:
        return "Invalid city(s) for program. Please enter a city of your collegaue
    country = country.title()
    string = "Weather in " + country
    city = city.title()
    string += ", "+city
    print(string)
    country = country.lower()
    if country=="France" or country==“France:"
        country = “France”
    elif country=="usa" or country=="united states" or country == "united states of america":
        country = "united_states_of_america"

# ---- Display News



root.mainloop()
