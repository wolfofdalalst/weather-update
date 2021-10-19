from tkinter import *
from tkinter import messagebox
from ctypes import windll
from datetime import datetime
from pickle import load, dump
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

        # configuring the window
        self.geometry('500x700')
        self.config(bg="#F0F3F4")
        self.resizable(0,0)

        # setting the window icon(top)
        windowlogo=PhotoImage(file=r"images/icon.png")
        self.iconphoto(True,windowlogo)

        # text field for user to enter
        self.city=Entry(self,width=25,font=("Cambria,bold",11))
        self.city.place(x=150,y=0)

        # setting the taskbar icon
        logo = r"images/icon.png" # arbitrary string
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(logo)

        # setting date,time and year
        dt=datetime.now() 
        currentdate=Label(self,text=dt.strftime('%A,'), bg='#F0F3F4',fg='black',font=("Cambria,bold",12))
        currentdate.place(x=160,y=160)
        month=Label(self,text=dt.strftime('%m %B'),bg='#F0F3F4',fg='black' ,font=("Cambria,bold",12))
        month.place(x=230,y=160)

        # space to receive city details
        self.location=Label(self, text="...",width=0,bg='#F0F3F4',fg='black', font=("bold", 20))
        self.location.place(x=225,y=100)

        # openweather icons
        icon=Label(self,text="... ",width=0,bg='#F0F3F4',font=("bold",50))
        icon.place(x=140,y=260)

        # space to receive temperature
        self.temperature = Label(self, text="...", width=0, bg='#F0F3F4',font=("Cambria,bold", 50), fg='black')
        self.temperature.place(x=270, y=260)

        # humidity
        humidity_display=Label(self,text="Humidity ",width=0,bg='#F0F3F4',fg='black',font=("Cambria,bold",12))
        humidity_display.place(x=100,y=400)

        # space to display humidity
        self.humidity=Label(self,text="...",width=0,bg='#F0F3F4',font=("bold,Cambria",15),fg="black")
        self.humidity.place(x=200,y=400)

        # UV index
        uvindex_display=Label(self,text="UV Index ",width=0,bg='#F0F3F4',fg='black',font=("Cambria,bold",12))
        uvindex_display.place(x=100,y=450)

        #space to display UV index
        uvindex=Label(self,text="...",width=0,bg='#F0F3F4',font=("bold,Cambria",15),fg="black")
        uvindex.place(x=200,y=450)

        # probability of rain
        rainprobability_display=Label(self,text="Probaility of rain ",width=0,bg='#F0F3F4',fg='black',font=("Cambria,bold",12))
        rainprobability_display.place(x=100,y=500)

        # space to display rain probability
        rainprobability=Label(self,text="...",width=0,bg='#F0F3F4',font=("bold,Cambria",15),fg="black")
        rainprobability.place(x=250,y=500)

         # pressure
        pressure_display=Label(self,text="Pressure ",width=0,bg='#F0F3F4',fg='black',font=("Cambria,bold",12))
        pressure_display.place(x=100,y=550)

        # space to display pressure
        self.pressure=Label(self,text="...",width=0,bg='#F0F3F4',font=("Cambria,bold",15), fg='black')
        self.pressure.place(x=200,y=550)

        self.main_method(city_name=Persistence.get_data())

        # search button
        self.button=Button(self, text="Search",bg="black",fg='white',font=("bold,12"))
        self.button["command"] = self.main_method
        self.button.place(x=300,y=0)

    def main_method(self, city_name=None):
        if city_name == None: city_name:str = self.city.get()
            # save the current input city name to data directory

        city_obj = CurrentCity(city_name, test=False)

        if city_obj.cod == "404": messagebox.showerror("Error","City not found")

        self.location['text'] = city_obj.name

        #self.des['text'] = city_obj.weather['main']
        #self.des['font'] = ('calibri',20,'bold')

        #self.description['text'] = city_obj.weather['description']
        #self.description['font'] = ('calibri',20,'bold')

        self.temperature['text'] = city_obj.temperature
        self.temperature['font'] = ('calibri',15,'bold')

        self.humidity['text'] = city_obj.humidity
        self.humidity['font'] = ('calibri',15,'bold')

        self.pressure['text'] = city_obj.pressure
        self.pressure['font'] = ('calibri',15,'bold')

        Persistence.set_data('Kolkata')


if __name__ == '__main__':
    weather = Weather()
    weather.mainloop()  