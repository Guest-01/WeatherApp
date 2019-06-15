import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600
API_KEY = ''  #Your API_KEY


# https://openweathermap.org/ check for your API_KEY
# api.openweathermap.org/data/2.5/weather?q={city name},{country code}
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}


def test_function(entry):
    print('This is the entry:', entry)


def format_response(weather):

    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_string = f'City:{name}\nConditions:{desc}\nTemperature(C):{temp}'

    except:
        final_string = '정보를 가져오는데 실패했습니다'

    return final_string


def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': API_KEY, 'q': city, 'units': 'Metric', 'lang': 'kr'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='light blue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='light blue', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('D2Coding', 15), anchor='nw', justify='left', bd=10)
label.place(relwidth=1, relheight=1)

root.mainloop()
