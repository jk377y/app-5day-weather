#! This is the code from the original weather api project. It was used as a reference for this project.

# import requests
# import json
# from datetime import datetime

# def kelvin_to_fahrenheit(kelvin_temp):
#     return round((kelvin_temp - 273.15) * 9/5 + 32, 2)

# def mps_to_mph(mps_speed):
#     return round(mps_speed * 2.237, 2)

# def weather():
#     print("=== 5-Day Weather Forecast ===")
#     city = input("Enter the name of a city: ")

#     api_key = "d01afd2806e508d282da4f840dd4696a"
#     base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

#     response = requests.get(base_url)
#     data = json.loads(response.text)

#     if data["cod"] == "404":
#         print(f"Weather information not found for '{city}'. Please try again.")
    
#     else:
#         forecasts = data["list"]
#         forecast_dates = []
#         daily_forecasts = {}

#         for forecast in forecasts:
#             forecast_datetime = datetime.fromtimestamp(forecast["dt"])
#             forecast_date = forecast_datetime.date()

#             if forecast_date not in forecast_dates:
#                 forecast_dates.append(forecast_date)
#                 daily_forecasts[forecast_date] = {
#                     "main_weather": forecast["weather"][0]["main"],
#                     "description": forecast["weather"][0]["description"],
#                     "temperature": kelvin_to_fahrenheit(forecast["main"]["temp"]),
#                     "humidity": forecast["main"]["humidity"],
#                     "wind_speed": mps_to_mph(forecast["wind"]["speed"])
#                 }

#         print((f"\n5-Day Weather Forecast for '{city}':").upper())
#         for date, forecast in daily_forecasts.items():
#             print(f"\nDate: {date}")
#             print((f"Main Weather: {forecast['main_weather']}").upper())
#             print((f"Description: {forecast['description']}").upper())
#             print(f"Temperature: {forecast['temperature']:.2f} °F")
#             print(f"Humidity: {forecast['humidity']}%")
#             print((f"Wind Speed: {forecast['wind_speed']} mph").upper())

# weather()

# import customtkinter as ctk # used to create custom tkinter widgets for the GUI
# import requests # used to make API requests
# import json # used to parse JSON data from API responses
# from datetime import datetime # used to convert UNIX timestamps to datetime objects

# def kelvin_to_fahrenheit(kelvin_temp):
#     return round((kelvin_temp - 273.15) * 9/5 + 32, 2)

# def mps_to_mph(mps_speed):
#     return round(mps_speed * 2.237, 2)

# class WeatherApp:
#     def __init__(self): # constructor method for the WeatherApp class 
#         self.city_label = None
#         self.result_labels = []
#         self.error_label = None

#     def create_window(self): # creates the main window for the GUI 
#         window = ctk.CTk()
#         window.title("5-Day Weather Forecast")
#         window.geometry("400x300")
#         window.grid_columnconfigure(0, weight=1)
#         window.iconbitmap("images/icons/sun.ico")
#         return window

#     def create_input_frame(self, window):
#         input_frame = ctk.CTkFrame(window)
#         input_frame.grid(row=0, column=0, pady=10)
#         input_frame.grid_columnconfigure(0, weight=1)

#         label = ctk.CTkLabel(input_frame, text="Enter the name of a city:", font=("Arial", 14))
#         label.grid(in_=input_frame, row=0, pady=5)

#         city_entry = ctk.CTkEntry(input_frame)
#         city_entry.grid(in_=input_frame, row=1, pady=5)

#         self.error_label = ctk.CTkLabel(input_frame, text="", text_color="red", font=("Arial", 12))
#         self.error_label.grid(in_=input_frame, row=2, pady=5)

#         return city_entry

#     def create_forecast_frame(self, window):
#         forecast_frame = ctk.CTkFrame(window)
#         forecast_frame.grid(row=3, column=0, pady=5, padx=10)
#         forecast_frame.grid_remove()
#         return forecast_frame

#     def destroy(self):
#         for label in self.result_labels:
#             label.destroy()
#         self.result_labels.clear()
#         self.error_label.configure(text="")
#         self.error_label.grid_remove()
#         self.forecast_frame.grid_remove()
#         self.window.geometry("400x300")
#         if self.city_label:
#             self.city_label.destroy()
#             self.city_label = None

#     def show_error(self, message):
#         error_message = self.error_label.cget("text")
#         if error_message:
#             error_message += "\n" + message
#         else:
#             error_message = message
#         self.error_label.configure(text=error_message)
#         self.error_label.grid()

#     class WeatherApp:
#         def __init__(self):
#             self.city_label = None
#             self.result_labels = []
#             self.error_label = None

#     def get_weather(self, event=None):
#         self.destroy()
#         city = self.city_entry.get()

#         api_key = "d01afd2806e508d282da4f840dd4696a"
#         base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

#         response = requests.get(base_url)
#         data = json.loads(response.text)
#         if self.city_entry.get() == "":
#             self.show_error("Please enter a city name.")
#         elif data["cod"] == "404":
#             error_message = f"Weather information not found for '{city}'.\nPlease try again."
#             self.show_error(error_message)
#             result_label = ctk.CTkLabel(self.forecast_frame, text="", font=("Arial", 14))
#             result_label.grid(row=0, column=0, pady=5, padx=20)
#         else:
#             forecasts = data["list"]
#             forecast_dates = []
#             daily_forecasts = {}

#             for forecast in forecasts:
#                 forecast_date = datetime.fromtimestamp(forecast["dt"]).date()

#                 if forecast_date not in forecast_dates:
#                     forecast_dates.append(forecast_date)
#                     daily_forecasts[forecast_date] = {
#                         "main_weather": forecast["weather"][0]["main"],
#                         "description": forecast["weather"][0]["description"],
#                         "temperature": kelvin_to_fahrenheit(forecast["main"]["temp"]),
#                         "humidity": forecast["main"]["humidity"],
#                         "wind_speed": mps_to_mph(forecast["wind"]["speed"])
#                     }

#             start_index = 7  # Starting index for forecast dates
#             forecast_dates = forecast_dates[start_index::]

#             column = 0

#             self.city_label = ctk.CTkLabel(self.forecast_frame, text=f"5-Day Weather Forecast for {city.title()}", font=("Arial", 16), text_color="yellow")
#             self.city_label.grid(row=0, column=0, columnspan=len(daily_forecasts), pady=5, padx=20)

#             for date, forecast in daily_forecasts.items():
#                 result_label = ctk.CTkLabel(self.forecast_frame,
#                                             text=f"\nDate: {date}\n\n"
#                                                  f"Main Weather: {forecast['main_weather'].upper()}\n"
#                                                  f"Description: {forecast['description'].upper()}\n"
#                                                  f"Temperature: {forecast['temperature']:.2f} °F\n"
#                                                  f"Humidity: {forecast['humidity']}%\n"
#                                                  f"Wind Speed: {forecast['wind_speed']} MPH\n",
#                                             font=("Arial", 14),
#                                             wraplength=250,
#                                             text_color="white",
#                                             fg_color="#196c92",
#                                             corner_radius=20,
#                                             padx=10,
#                                             pady=10,
#                                             justify="center")

#                 result_label.grid(row=1, column=column, pady=10, padx=10)
#                 self.result_labels.append(result_label)
#                 column += 1

#             self.window.geometry("1600x500")
#             self.forecast_frame.grid()
#             self.window.update()

#     def create_buttons_frame(self, window):
#         buttons_frame = ctk.CTkFrame(window)
#         buttons_frame.grid(row=2, column=0, pady=10)

#         button = ctk.CTkButton(window, text="Get Weather", command=self.get_weather)
#         button.grid(in_=buttons_frame, row=0, pady=5)

#         self.city_entry.bind("<Return>", self.get_weather)

#         button = ctk.CTkButton(window, text="Reset", command=self.destroy)
#         button.grid(in_=buttons_frame, row=1, pady=5)

#     def run(self):
#         self.window = self.create_window()
#         self.city_entry = self.create_input_frame(self.window)
#         self.forecast_frame = self.create_forecast_frame(self.window)
#         self.create_buttons_frame(self.window)
#         self.window.mainloop()

# def main():
#     weather_app = WeatherApp()
#     weather_app.run()

# if __name__ == "__main__":
#     main()


from tkinter import *
import customtkinter as ctk # used to create custom widgets and frames
import requests # used to make API requests
import json # used to parse JSON data from API responses
from datetime import datetime # used to convert UNIX timestamps to datetime objects
from PIL import Image, ImageTk
import PIL.Image
import PIL.ImageTk
import io

#! Window
# ===================================================================
window = ctk.CTk()
window.geometry("500x350")
window.title("5-Day Weather Forecast")
ctk.set_appearance_mode("dark")
window.grid_columnconfigure(0, weight=1)
window.iconbitmap("images/icons/sun.ico")
# ===================================================================

#! Title Frame
# ===================================================================
title_frame = ctk.CTkFrame(window, fg_color="transparent")
title_frame.grid(row=0, column=0, pady=10)
title_label = ctk.CTkLabel(title_frame, text="5-Day Weather Forecast", font=("Arial", 32), text_color="#00a2ff")
title_label.grid(row=0, column=0, pady=15)
# ===================================================================

#! Top Frame
# ===================================================================
top_frame = ctk.CTkFrame(window)
top_frame.grid(row=1, column=0, pady=10)

top_left_frame = ctk.CTkFrame(top_frame)
top_left_frame.grid(row=0, column=0, pady=10, padx=10, sticky="ew")
instruction_label = ctk.CTkLabel(top_left_frame, text="Enter a city:", font=("Arial", 16), text_color="white")
instruction_label.grid(row=0, column=0, pady=10, padx=10)
city_entry = ctk.CTkEntry(top_left_frame, font=("Arial", 16), corner_radius=10)
city_entry.grid(row=1, column=0, pady=10, padx=10)

top_right_frame = ctk.CTkFrame(top_frame, fg_color="#113874", corner_radius=10)
top_right_frame.grid(row=0, column=1, pady=10, padx=10, sticky="ew")
top_right_frame.grid_remove()
    # current weather data elements assigned here; see below
# ===================================================================

#! Bottom Frame
# ===================================================================
bottom_frame = ctk.CTkFrame(window, fg_color="#113874", corner_radius=10)
bottom_frame.grid(row=3, column=0, pady=10)
bottom_frame.grid_remove()
    # forecast data elements assigned here; see for loop below 
# ===================================================================

#!  def get_weather():
# ===================================================================
def get_weather(event=None):
    def kelvin_to_fahrenheit(kelvin_temp):
        return round((kelvin_temp - 273.15) * 9/5 + 32, 2)
    def mps_to_mph(mps_speed):
        return round(mps_speed * 2.237, 2)
    for label in top_right_frame.grid_slaves():
        label.grid_forget()
    for label in bottom_frame.grid_slaves():
        label.grid_forget()
    for error_label in top_left_frame.grid_slaves():
        if error_label.grid_info()["row"] == 4:
            error_label.grid_forget()
    city = city_entry.get()
    if city == "":
        error_label = ctk.CTkLabel(top_left_frame, text="Field cannot be blank.", font=("Arial", 16), text_color="white")
        error_label.grid(row=4, column=0, pady=10, padx=10)
        return
    api_key = "d01afd2806e508d282da4f840dd4696a"
    base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = json.loads(response.text)
    if data["cod"] == "404":
        error_label = ctk.CTkLabel(top_left_frame, text="Please enter a valid city (404).", font=("Arial", 16), text_color="white")
        error_label.grid(row=4, column=0, pady=10, padx=10)
        return
    if data["cod"] == "400":
        error_label = ctk.CTkLabel(top_left_frame, text="Please enter a valid city. (400)", font=("Arial", 16), text_color="white")
        error_label.grid(row=4, column=0, pady=10, padx=10)
        return
    city_name = data["city"]["name"].upper()
    current_data = data["list"][0]
    current_date = datetime.utcfromtimestamp(current_data["dt"]).strftime("%m-%d-%Y")
    current_description = current_data["weather"][0]["description"].upper()
    current_temperature = kelvin_to_fahrenheit(current_data["main"]["temp"])
    current_humidity = current_data["main"]["humidity"]
    current_wind = mps_to_mph(current_data["wind"]["speed"])

    top_right_frame.grid()
    bottom_frame.grid()
    window.geometry("1250x725")

    current_weather_icon_link = f"http://openweathermap.org/img/wn/{current_data['weather'][0]['icon']}@2x.png"
    response = requests.get(current_weather_icon_link)
    img_data = response.content
    img = PIL.Image.open(io.BytesIO(img_data))
    img = img.resize((100, 100))
    current_weather_icon = PIL.ImageTk.PhotoImage(img)
    current_weather_icon_label = ctk.CTkLabel(top_left_frame, image=current_weather_icon)
    current_weather_icon_label.grid(row=2, column=0, pady=10, padx=10)

    current_city_label = ctk.CTkLabel(top_right_frame, text=f"{city_name}", font=("Arial", 20, "bold"), text_color="white")
    current_city_label.grid(row=0, column=0, pady=10, padx=10)
    current_date_label = ctk.CTkLabel(top_right_frame, text=f"{current_date}", font=("Arial", 18), text_color="white")
    current_date_label.grid(row=1, column=0, padx=10)
    current_description_label = ctk.CTkLabel(top_right_frame, text=f"{current_description}", font=("Arial", 16), text_color="white")
    current_description_label.grid(row=2, column=0, padx=10)
    current_temperature_label = ctk.CTkLabel(top_right_frame, text=f"Temperature: {current_temperature} °F", font=("Arial", 16), text_color="white")
    current_temperature_label.grid(row=3, column=0, padx=10)
    current_humidity_label = ctk.CTkLabel(top_right_frame, text=f"Humidity: {current_humidity} %", font=("Arial", 16), text_color="white")
    current_humidity_label.grid(row=4, column=0, padx=10)
    current_wind_label = ctk.CTkLabel(top_right_frame, text=f"Wind: {current_wind} MPH", font=("Arial", 16), text_color="white")
    current_wind_label.grid(row=5, column=0, padx=10)
    
    forecast_data = data["list"][7::8]
    column_padding = 30  # Adjust this value to control the gap between columns

    for i, forecast in enumerate(forecast_data):
        unix_date = forecast["dt"]
        formatted_date = datetime.utcfromtimestamp(unix_date).strftime("%m-%d-%Y")
        description = forecast["weather"][0]["description"].upper()
        temperature = kelvin_to_fahrenheit(forecast["main"]["temp"])
        humidity = forecast["main"]["humidity"]
        wind = mps_to_mph(forecast["wind"]["speed"])

        forecast_label_date = ctk.CTkLabel(bottom_frame, text=f"{formatted_date}\n", font=("Arial", 20), text_color="white")
        forecast_label_date.grid(row=0, column=i, pady=20, padx=column_padding)
        forecast_label_description = ctk.CTkLabel(bottom_frame, text=f"{description}", font=("Arial", 18), text_color="white")
        forecast_label_description.grid(row=1, column=i, pady=5, padx=column_padding)
        forecast_label_temperature = ctk.CTkLabel(bottom_frame, text=f"Temperature: {temperature} °F", font=("Arial", 16), text_color="white")
        forecast_label_temperature.grid(row=2, column=i, pady=5, padx=column_padding)
        forecast_label_humidity = ctk.CTkLabel(bottom_frame, text=f"Humidity: {humidity} %", font=("Arial", 16), text_color="white")
        forecast_label_humidity.grid(row=3, column=i, pady=5, padx=column_padding)
        forecast_label_wind = ctk.CTkLabel(bottom_frame, text=f"Wind: {wind} MPH", font=("Arial", 16), text_color="white")
        forecast_label_wind.grid(row=4, column=i, pady=5, padx=column_padding)
# ===================================================================

#! Middle Frame Layout
# ===================================================================
middle_frame = ctk.CTkFrame(window)
middle_frame.grid(row=2, column=0, pady=10)
fetch_button = ctk.CTkButton(middle_frame, text="Get Weather", font=("Arial", 18, "bold"), text_color="white", fg_color="#113874", corner_radius=15, command=get_weather)
fetch_button.grid(row=0, column=0, pady=10, padx=10)
# ===================================================================

city_entry.bind("<Return>", get_weather)


window.mainloop()
