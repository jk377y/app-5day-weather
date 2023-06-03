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

# import customtkinter as ctk
# from customtkinter import CTkFont
# from tkinter import font as tkfont
# import requests
# import json
# from datetime import datetime

# def kelvin_to_fahrenheit(kelvin_temp):
#     return round((kelvin_temp - 273.15) * 9/5 + 32, 2)

# def mps_to_mph(mps_speed):
#     return round(mps_speed * 2.237, 2)

# def weather():
#     window = ctk.CTk()  # create the main window
#     window.title("5-Day Weather Forecast")  # set the title of the main window
#     window.geometry("400x300")  # set the size of the main window
#     window.grid_columnconfigure(0, weight=1)  # set column 0 to stretch if the window is resized

#     input_frame = ctk.CTkFrame(window)
#     input_frame.grid(row=0, column=0, pady=10)
#     input_frame.grid_columnconfigure(0, weight=1)

#     label = ctk.CTkLabel(input_frame, text="Enter the name of a city:", font=("Arial", 14))
#     label.grid(in_=input_frame, row=0, pady=5)

#     city_entry = ctk.CTkEntry(input_frame)
#     city_entry.grid(in_=input_frame, row=1, pady=5)

#     error_label = ctk.CTkLabel(input_frame, text="", text_color="red", font=("Arial", 12))
#     error_label.grid(in_=input_frame, row=2, pady=5)




#     forecast_frame = ctk.CTkFrame(window)  # create the forecast frame
#     forecast_frame.grid(row=3, column=0, pady=5, padx=10)
#     forecast_frame.grid_remove()  # hide the forecast frame until the user enters a city name

#     result_labels = []  # store the result labels for each day

#     def destroy():
#         # city_entry.delete(0, "end")
#         for label in result_labels:
#             label.destroy()
#         result_labels.clear()
#         error_label.configure(text="")
#         error_label.grid_remove()
#         forecast_frame.grid_remove()
#         window.geometry("400x300")

#     def show_error(message):
#         error_label.configure(text="")
#         error_message = error_label.cget("text")
#         if error_message:
#             error_message += "\n" + message
#         else:
#             error_message = message
#         error_label.configure(text=error_message)
#         error_label.grid()

#     def get_weather(event=None):
#         destroy()
#         city = city_entry.get()
        
#         api_key = "d01afd2806e508d282da4f840dd4696a"
#         base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

#         response = requests.get(base_url)
#         data = json.loads(response.text)
#         if city_entry.get() == "":
#             show_error("Please enter a city name.")
#         elif data["cod"] == "404":
#             error_message = f"Weather information not found for '{city}'.\n Please try again."
#             show_error(error_message)
#             result_label = ctk.CTkLabel(forecast_frame, text="", font=("Arial", 14))
#             result_label.grid(row=0, column=0, pady=5, padx=20)
#         else:
#             forecasts = data["list"]
#             forecast_dates = []
#             daily_forecasts = {}
#             error_label.grid_remove()

#             for forecast in forecasts:
#                 forecast_datetime = datetime.fromtimestamp(forecast["dt"])
#                 forecast_date = forecast_datetime.date()

#                 if forecast_date not in forecast_dates:
#                     forecast_dates.append(forecast_date)
#                     daily_forecasts[forecast_date] = {
#                         "main_weather": forecast["weather"][0]["main"],
#                         "description": forecast["weather"][0]["description"],
#                         "temperature": kelvin_to_fahrenheit(forecast["main"]["temp"]),
#                         "humidity": forecast["main"]["humidity"],
#                         "wind_speed": mps_to_mph(forecast["wind"]["speed"])
#                     }

#             column = 0

#             city_label = ctk.CTkLabel(forecast_frame, text=f"5-Day Weather Forecast for {city.title()}", font=("Arial", 16), text_color="yellow")
#             city_label.grid(row=0, column=0, columnspan=len(daily_forecasts), pady=5, padx=20)
        
#             for date, forecast in daily_forecasts.items():
#                 result_label = ctk.CTkLabel(forecast_frame, 
#                                             text=f"\nDate: {date}\n\n"
#                                                                   f"Main Weather: {forecast['main_weather'].upper()}\n"
#                                                                   f"Description: {forecast['description'].upper()}\n"
#                                                                   f"Temperature: {forecast['temperature']:.2f} °F\n"
#                                                                   f"Humidity: {forecast['humidity']}%\n"
#                                                                   f"Wind Speed: {forecast['wind_speed']} mph\n",
#                                             font=("Arial", 14), 
#                                             wraplength=250, 
#                                             text_color="white", 
#                                             fg_color="#196c92",
#                                             corner_radius=20, 
#                                             padx=10, 
#                                             pady=10, 
#                                             justify="center")
                
#                 result_label.grid(row=1, column=column, pady=10, padx=10)
#                 result_labels.append(result_label)
#                 column += 1
            
#             window.geometry("1600x500")
#             forecast_frame.grid()
#             window.update()


#     buttons_frame = ctk.CTkFrame(window)
#     buttons_frame.grid(row=2, column=0, pady=10)

#     button = ctk.CTkButton(window, text="Get Weather", command=get_weather)
#     button.grid(in_=buttons_frame, row=0, pady=5)
#     city_entry.bind("<Return>", get_weather)

#     button = ctk.CTkButton(window, text="Reset", command=destroy)
#     button.grid(in_=buttons_frame, row=1, pady=5)

#     window.mainloop()

# weather()


import customtkinter as ctk
from customtkinter import CTkFont
from tkinter import font as tkfont
import requests
import json
from datetime import datetime

def kelvin_to_fahrenheit(kelvin_temp):
    return round((kelvin_temp - 273.15) * 9/5 + 32, 2)

def mps_to_mph(mps_speed):
    return round(mps_speed * 2.237, 2)

def weather():
    global city_label  # Declare city_label as a global variable
    city_label = None  # store the city label widget

    window = ctk.CTk()  # create the main window
    window.title("5-Day Weather Forecast")  # set the title of the main window
    window.geometry("400x300")  # set the size of the main window
    window.grid_columnconfigure(0, weight=1)  # set column 0 to stretch if the window is resized
    window.iconbitmap("images/icons/sun.ico")

    input_frame = ctk.CTkFrame(window)
    input_frame.grid(row=0, column=0, pady=10)
    input_frame.grid_columnconfigure(0, weight=1)

    label = ctk.CTkLabel(input_frame, text="Enter the name of a city:", font=("Arial", 14))
    label.grid(in_=input_frame, row=0, pady=5)

    city_entry = ctk.CTkEntry(input_frame)
    city_entry.grid(in_=input_frame, row=1, pady=5)

    error_label = ctk.CTkLabel(input_frame, text="", text_color="red", font=("Arial", 12))
    error_label.grid(in_=input_frame, row=2, pady=5)

    forecast_frame = ctk.CTkFrame(window)  # create the forecast frame
    forecast_frame.grid(row=3, column=0, pady=5, padx=10)
    forecast_frame.grid_remove()  # hide the forecast frame until the user enters a city name

    result_labels = []  # store the result labels for each day

    def destroy():
        global city_label
        for label in result_labels:
            label.destroy()
        result_labels.clear()
        error_label.configure(text="")
        error_label.grid_remove()
        forecast_frame.grid_remove()
        window.geometry("400x300")
        if city_label:
            city_label.destroy()
            city_label = None

    def show_error(message):
        error_label.configure(text="")
        error_message = error_label.cget("text")
        if error_message:
            error_message += "\n" + message
        else:
            error_message = message
        error_label.configure(text=error_message)
        error_label.grid()

    def get_weather(event=None):
        global city_label
        destroy()
        city = city_entry.get()
        
        api_key = "d01afd2806e508d282da4f840dd4696a"
        base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

        response = requests.get(base_url)
        data = json.loads(response.text)
        if city_entry.get() == "":
            show_error("Please enter a city name.")
        elif data["cod"] == "404":
            error_message = f"Weather information not found for '{city}'.\n Please try again."
            show_error(error_message)
            result_label = ctk.CTkLabel(forecast_frame, text="", font=("Arial", 14))
            result_label.grid(row=0, column=0, pady=5, padx=20)
        else:
            forecasts = data["list"]
            forecast_dates = []
            daily_forecasts = {}
            error_label.grid_remove()

            for forecast in forecasts:
                forecast_datetime = datetime.fromtimestamp(forecast["dt"])
                forecast_date = forecast_datetime.date()

                if forecast_date not in forecast_dates:
                    forecast_dates.append(forecast_date)
                    daily_forecasts[forecast_date] = {
                        "main_weather": forecast["weather"][0]["main"],
                        "description": forecast["weather"][0]["description"],
                        "temperature": kelvin_to_fahrenheit(forecast["main"]["temp"]),
                        "humidity": forecast["main"]["humidity"],
                        "wind_speed": mps_to_mph(forecast["wind"]["speed"])
                    }

            column = 0

            city_label = ctk.CTkLabel(forecast_frame, text=f"5-Day Weather Forecast for {city.title()}", font=("Arial", 16), text_color="yellow")
            city_label.grid(row=0, column=0, columnspan=len(daily_forecasts), pady=5, padx=20)
        
            for date, forecast in daily_forecasts.items():
                result_label = ctk.CTkLabel(forecast_frame, 
                                            text=f"\nDate: {date}\n\n"
                                                                  f"Main Weather: {forecast['main_weather'].upper()}\n"
                                                                  f"Description: {forecast['description'].upper()}\n"
                                                                  f"Temperature: {forecast['temperature']:.2f} °F\n"
                                                                  f"Humidity: {forecast['humidity']}%\n"
                                                                  f"Wind Speed: {forecast['wind_speed']} mph\n",
                                            font=("Arial", 14), 
                                            wraplength=250, 
                                            text_color="white", 
                                            fg_color="#196c92",
                                            corner_radius=20, 
                                            padx=10, 
                                            pady=10, 
                                            justify="center")
                
                result_label.grid(row=1, column=column, pady=10, padx=10)
                result_labels.append(result_label)
                column += 1
            
            window.geometry("1600x500")
            forecast_frame.grid()
            window.update()

    buttons_frame = ctk.CTkFrame(window)
    buttons_frame.grid(row=2, column=0, pady=10)

    button = ctk.CTkButton(window, text="Get Weather", command=get_weather)
    button.grid(in_=buttons_frame, row=0, pady=5)
    city_entry.bind("<Return>", get_weather)

    button = ctk.CTkButton(window, text="Reset", command=destroy)
    button.grid(in_=buttons_frame, row=1, pady=5)

    window.mainloop()

weather()