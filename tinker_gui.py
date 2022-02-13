import os
from tkinter import *
from tkinter import messagebox
from urllib.request import urlopen
from newsweather import weather, news
from PIL import Image, ImageTk
#from country_list import countries_for_language

colleagues = []

crt_path = os.getcwd()

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
root.geometry('900x500')

# ---- Create left and right frames

left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0,  padx=20, pady=5)

right_frame = Frame(root, width=650, height=500)
right_frame.grid(row=0, column=1, padx=10, pady=5)

#---- Images ----
im = Label(root, bitmap="")
im.grid(row=0, column=1, pady=5, columnspan=2)

im['bitmap'] = crt_path+"/Desktop/have_you_got_the_guts_project/Earth.png"

# ------- LEFT FRAME ----------

#Load logo
Logo = Image.open(crt_path+"/Desktop/have_you_got_the_guts_project/Logo.png")

#resize logo
resized = Logo.resize((300, 100), Image.ANTIALIAS)

new_Logo = ImageTk.PhotoImage(resized)

label = Label(
    root,
    image=new_Logo)
label.place(x=40, y=15)

# ---- Add Colleague
add_colleague_label = Label(left_frame, text="Add Colleague").grid(row=1, column=0, pady=5, columnspan=2)

# ---- name information ----
name_label = Label(left_frame, text="Name:")
name_label.grid(row=2, column=0, pady=5)

name_entry = Entry(left_frame)
name_entry.focus_set()
name_entry.grid(row=2, column=1, pady=5)

# ---- city information ----
def on_click_cit(event):
    city_entry.configure(state=NORMAL)
    city_entry.delete(0, END)

    # make the callback only work once
    city_entry.unbind('<Button-1>', on_click_city)

city_label = Label(left_frame, text="City:")
city_label.grid(row=3, column=0, pady=5)

#location_label = Label(left_frame, text="Location:")
#location_label.grid(row=2, column=0, pady=5)

city_entry = Entry(left_frame)
city_entry.insert(0, "Insert City...")
city_entry.focus_set()
city_entry.grid(row=3, column=1, padx=5, pady=5)

on_click_city = city_entry.bind('<Button-1>', on_click_cit)

# ---- country information ----
def on_click_count(event):
    country_entry.configure(state=NORMAL)
    country_entry.delete(0, END)

    # make the callback only work once
    country_entry.unbind('<Button-1>', on_click_country)

country_label = Label(left_frame, text="Country:")
country_label.grid(row=4, column=0, pady=5)

country_entry = Entry(left_frame)
country_entry.insert(0, "Insert Country...")
country_entry.focus_set()
country_entry.grid(row=4, column=1, padx=5, pady=5)

on_click_country = country_entry.bind('<Button-1>', on_click_count)

# ---- add button ----
add_colleague_button = Button(left_frame, text="Add", command=add_colleague_to_list)
add_colleague_button.grid(row=5, column=0, pady=5, columnspan=2)

# ---- confirmation ----
confirmation_label = Label(left_frame, text="")
confirmation_label.grid(row=6, column=0, pady=5, columnspan=2)


# ---- Select Colleague Drop Down Menu ----

existing_colleague_label = Label(left_frame, text="Select Existing Colleague")
existing_colleague_label.grid(row=7, column=0, pady=5, columnspan=2)

clicked = StringVar()
clicked.set("Select...") # default value

#colleagues

def clear_label_image():
        im.destroy()

def callback(*choices):
    clear_label_image()

    #space = Label(left_frame, text="")
    #space.grid(row=0, column=0, pady=0)

    basic_font_color = "#ccc4c4"
    bg_color_weather = "#00adad"
    bg_color_news = "#a6a8a6"

    Weather_Display = Label(right_frame, text="", font=("times new roman", 30, "bold"), bg=bg_color_weather,
        fg=basic_font_color, bd=10, relief=GROOVE)
    Weather_Display.place(x=80, y=10, width=480, relheight=0.4)

    News_Display = Label(right_frame, text="", font=("times new roman", 30, "bold"), bg=bg_color_news,
        fg=basic_font_color, bd=10, relief=GROOVE)
    News_Display.place(x=80, y=250, width=480, relheight=0.4)



choices = ['op1', 'op2']
#*colleagues

colleague_drop = OptionMenu(left_frame, clicked, *choices, command=callback)
colleague_drop.grid(row=8, column=0, pady=5, columnspan=2)

# ------- Right FRAME ----------
# ---- Display Weather
def display_weather(name):
    n_index = colleagues.index(name)
    country = colleagues[n_index+2]
    city = colleagues[n_index+1]
    output = weather(country, city)
    return output


# ---- Display News
def display_news(name):
    world_headers = ['africa', 'asia', 'australia', 'europe', 'latin america', 'middle east', 'us & canada']
    home_headers = ['england', 'northern ireland', 'scotland', 'wales']
    n_index = colleagues.index(name)
    country = colleagues[n_index+2]
    if country.lower() in home_headers or country.lower() == 'united kingdom' or country.lower() == 'uk':
        country = 'united kingdom'
    elif country.title() in EUROPEAN_UNION.names:
        country = 'europe'
    output = news(country)
    return output


def on_closing():
    if messagebox.askokcancel("Quit", "Would you like to exit the programme?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
