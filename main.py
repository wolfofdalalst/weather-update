from tkinter import *
from tkinter import messagebox
from ctypes import windll
from datetime import datetime
from pickle import load, dump
from PIL import ImageTk
from time import time

from open_weather.current import CurrentCity

class City:
    def __init__(self, city_name:str):
        self.city_name:str = city_name
        self.time = time()

class Persistence:
    @staticmethod
    def set_data(city_name:str) -> None:
        city = City(city_name)
        with open('data/record.txt', 'wb') as file_obj:
            dump(city, file_obj)

    @staticmethod
    def get_data() -> str:
        try:
            with open('data/record.txt', 'rb') as file_obj:
                data = load(file_obj)
        except EOFError:
            Persistence.set_data('Kolkata')
            print('setting initial data to => KOLKATA')

        return data.city_name

class Weather(Tk):

    def __init__(self):
        super().__init__()
        global background_image

        self.geometry('576x700')
        self.resizable(0,0)
        self.title("AuraX")

        # setting the window icon(top)
        windowlogo=PhotoImage(file=r"images/icon.png")
        self.iconphoto(True,windowlogo)

        # setting the taskbar icon
        logo = r"images/icon.png" # arbitrary string
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(logo)

        
        background_image=ImageTk.PhotoImage(file=r"images/clouds4.jpg")
        panel=Label(self,image=background_image,bg='white')
        panel.place(x=0,y=0)
        

        self.city=Text(self,width=42,height=1,font=('Cambria',20,'bold'))
        self.city.place(x=230,y=50)

        self.temperature=Label(self,text='20*C',width=0,bg='white',fg='black',font=('Cambria',80,'bold'))
        self.temperature.place(x=50,y=200)

        self.location=Label(self, text="SAN FRANCISCO",width=0,bg='black',fg='white', font=('Cambria',20,'bold'))
        self.location.place(x=350,y=200)

        self.date=Label(self,text=datetime.now().date(),bg="black",fg="white",font=('Cambria',20,'bold'))
        self.date.place(x=350,y=240)

        self.pressure_display=Label(self,text="PRESSURE: ",width=0,bg='white',fg='black',font=('Cambria',20,'bold'))
        self.pressure_display.place(x=50,y=500)

        self.pressure=Label(self,text="...",width=0,bg='white',fg='black',font=('Cambria',20,'bold'))
        self.pressure.place(x=200,y=500)

        self.humidity_display=Label(self,text="HUMIDITY: ",width=0,bg='black',fg='white',font=("Cambria",20,"bold"))
        self.humidity_display.place(x=350,y=500)

        # space to display humidity
        self.humidity=Label(self,text="...",width=0,bg='black',font=("bold,Cambria",20),fg="white")
        self.humidity.place(x=500,y=500)

        self.visibility_display=Label(self,text="VISIBILITY: ",width=0,bg='black',fg='white',font=("Cambria",20,'bold'))
        self.visibility_display.place(x=50,y=600)

        # space to display visibility
        self.visibility=Label(self,text="...",width=0,bg='black',font=("Cambria",20,'bold'), fg='white')
        self.visibility.place(x=200,y=600)

        # UV index
        self.feels_like_display=Label(self,text="FEELS LIKE ",width=0,bg='#F0F3F4',fg='black',font=('Cambria',20,'bold'))
        self.feels_like_display.place(x=350,y=600)

        #space to display UV index
        self.feels_like=Label(self,text="...",width=0,bg='#F0F3F4',font=('Cambria',20,'bold'),fg="black")
        self.feels_like.place(x=490,y=600)

        self.main_method(city_name=Persistence.get_data())

        # search button
        self.button=Button(self, text="Search",bg="black",fg='white',font=("bold,12"))
        self.button["command"] = self.main_method
        self.button.place(x=300,y=0)

    def main_method(self, city_name=None):
        degree_celcius = "°C"
        if city_name == None: city_name:str = self.city.get("1.0", END)
            # save the current input city name to data directory

        city_obj = CurrentCity(city_name, test=False)

        if city_obj.cod == "404": messagebox.showerror("Error","City not found")

        self.location['text'] = city_obj.name

        #self.des['text'] = city_obj.weather['main']
        #self.des['font'] = ('calibri',20,'bold')

        #self.description['text'] = city_obj.weather['description']
        #self.description['font'] = ('calibri',20,'bold')

        self.temperature['text'] = str(city_obj.temperature)+degree_celcius

        self.humidity['text'] = city_obj.humidity
        # self.humidity['font'] = ('calibri',15,'bold')

        self.pressure['text'] = city_obj.pressure
        self.feels_like['text'] = str(city_obj.feels_like)+degree_celcius
        self.visibility['text'] = city_obj.visibility
        # self.pressure['font'] = ('calibri',15,'bold')

        Persistence.set_data('Kolkata')


if __name__ == '__main__':
    weather = Weather()
    weather.mainloop()  