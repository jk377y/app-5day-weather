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




import customtkinter as ctk
import requests
import json
from datetime import datetime

def WeatherApp():
    def kelvin_to_fahrenheit(kelvin_temp):
        return round((kelvin_temp - 273.15) * 9/5 + 32, 2)

    def mps_to_mph(mps_speed):
        return round(mps_speed * 2.237, 2)

    window = ctk.CTk()
    window.title("5-Day Weather Forecast")
    window.geometry("600x600")
    window.grid_columnconfigure(0, weight=1)
    window.iconbitmap("images/icons/sun.ico")

    label = ctk.CTkLabel(window, text="Enter the name of a city:", font=("Arial", 14))
    label.grid(row=0, column=0, pady=5)

    city_entry = ctk.CTkEntry(window)
    city_entry.grid(row=1, column=0, pady=5)

    error_label = ctk.CTkLabel(window, text="", text_color="red", font=("Arial", 12))
    error_label.grid(row=2, column=0, pady=5)

    current_weather_label = ctk.CTkLabel(window, text="", font=("Arial", 14), fg_color="green", corner_radius=20)
    current_weather_label.grid(row=0, column=1, rowspan=3, pady=5, padx=10)
    current_weather_label.grid_remove()

    forecast_frame = ctk.CTkFrame(window)
    forecast_frame.grid(row=3, column=0, columnspan=2, pady=5)

    result_labels = []

    def destroy():
        pass

    def show_error(message):
        pass

    def display_current_weather(current):
        timestamp = datetime.fromtimestamp(current['dt'])
        formatted_date = timestamp.strftime("%m-%d-%Y")
        city = city_entry.get().upper()
        current_weather_label.configure(
            text=f"{city}\n"
            f"\nDate: {formatted_date}\n\n"
            f"Main Weather: {current['weather'][0]['main']}\n"
            f"Description: {current['weather'][0]['description']}\n"
            f"Temperature: {kelvin_to_fahrenheit(current['main']['temp'])} °F\n"
            f"Humidity: {current['main']['humidity']}%\n"
            f"Wind Speed: {mps_to_mph(current['wind']['speed'])} MPH\n",
            padx=10,
            pady=10,
        )
        current_weather_label.grid(row=0, column=1, pady=5, padx=20)

    def display_forecast_weather(self, future):
        for label in forecast_frame.grid_slaves():
            label.grid_remove()

        for i, forecast in enumerate(future):
            formatted_date = datetime.fromtimestamp(forecast['dt']).strftime("%m-%d-%Y")
            forecast_label = ctk.CTkLabel(
                forecast_frame,
                text=f"\nDate: {formatted_date}\n"
                f"Main Weather: {forecast['weather'][0]['main']}\n"
                f"Description: {forecast['weather'][0]['description']}\n"
                f"Temperature: {kelvin_to_fahrenheit(forecast['main']['temp'])} °F\n"
                f"Humidity: {forecast['main']['humidity']}%\n"
                f"Wind Speed: {mps_to_mph(forecast['wind']['speed'])} MPH\n",
                font=("Arial", 14),
                padx=10,
                pady=10,
            )
            forecast_label.grid(row=0, column=0, pady=5, padx=10)

    def get_weather(self, event=None):
        city = self.city_entry.get()

        api_key = "d01afd2806e508d282da4f840dd4696a"
        base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

        response = requests.get(base_url)
        data = json.loads(response.text)
        if city_entry.get() == "":
            show_error("Please enter a city name.")
        elif data["cod"] == "404":
            error_message = f"Weather information not found for '{city}'.\nPlease try again."
            show_error(error_message)
            result_label = ctk.CTkLabel(forecast_frame, text="", font=("Arial", 14))
            result_label.grid(row=0, column=0, pady=5, padx=20)
        else:
            current = data["list"][0]
            future = []

            for i in range(7, len(data["list"]), 8):
                future.append(data["list"][i])

            display_current_weather(current)
            display_forecast_weather(future)
            current_weather_label.grid()

    def create_buttons_frame(self, window):
        buttons_frame = ctk.CTkFrame(window)
        buttons_frame.grid(row=2, column=0, pady=10)

        button = ctk.CTkButton(window, text="Get Weather", command=self.get_weather)
        button.grid(in_=buttons_frame, row=0, pady=5)

        self.city_entry.bind("<Return>", self.get_weather)

        button = ctk.CTkButton(window, text="Reset", command=self.destroy)
        button.grid(in_=buttons_frame, row=1, pady=5)

WeatherApp()