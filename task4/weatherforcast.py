from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
from PIL import Image, ImageTk  # Import ImageTk from PIL
import pytz

root = Tk()
root.title("Weather App")
root.configure(bg="white")
root.geometry("450x250+80+60")
root.resizable(False, False)

# Load the image using PIL
search_image = Image.open("./task4/searchbar.jpg")
search_image_tk = ImageTk.PhotoImage(search_image)
myimage = Label(image=search_image_tk)
myimage.place(x=20, y=20)

def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geopiExercises")  # Fixed the variable name
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")  # Corrected the strftime format
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER 🌙")

name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25), bg="white", border=0, fg="black")
textfield.place(x=40, y=40)
textfield.focus()


# Add a Button to trigger the getWeather function
button = Button(root, text="Get Weather", relief="groove", command=getWeather)
button.place(x=360, y=120)

root.mainloop()