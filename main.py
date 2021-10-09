from tkinter import * 
from tkinter import messagebox
import datetime 
import tkinter as tk
from open_weather import current

from open_weather.current import CurrentCity

class Weather(tk.Tk):

    @property
    def font(self):
        return ('calibri',20,'bold')
    
    def __init__(self):
        super().__init__()

        # configure the root window
        self.geometry('500x700')
        self.title("WEATHER REPORT")
        self.config(bg='black')
        
        # add location
        self.location=Label(self,text="NA-/",bg="black",fg="white",font=self.font)
        self.location.place(x=0,y=0)

        # add heading
        self.heading=Label(self,text="Weather Report",bg="black",fg="white",font=self.font)
        self.heading.place(x=180,y=0)
        
        # date,time,month label
        dt=datetime.datetime.now()
        currentdate=Label(self,text=dt.strftime('%A--'),bg='black',fg='orange',font=("bold ",15))
        currentdate.place(x=5,y=230)
        month=Label(self,text=dt.strftime('%m%B'),bg='black',fg='orange',font=("bold ",15))
        month.place(x=95,y=230)
        hour=Label(self,text=dt.strftime('%I : %M %p'),bg='white',font=("bold",15))
        hour.place(x=10,y=160)
        
        # add name
        self.name=Label(self,text="Enter City or Country name ",fg='orange',bg='black',font=self.font)
        self.name.place(x=100,y=35)

        self.text_box=Text(self,width=25,height=2)
        self.text_box.place(x=150,y=75)       
        

       # city name
        city_name=Label(self,text="....",width=0,bg='black',fg='orange',font=("bold,15"))
        city_name.place(x=0,y=100)

        # temperature
        temperature=Label(self,text="...",width=0,bg="black",font=("Helvetica",15), fg="orange")
        temperature.place(x=18,y=300)

        # maximum temperature
        maxtemp=Label(self,text="MAXIMUM TEMPERATURE: ",width=0,bg="black",fg="orange",font=("bold,15"))
        maxtemp.place(x=0,y=400)

        # maximum temperature
        temperature=Label(self,text="...",width=0,bg="black",font=("Helvetica",15),fg="orange")
        temperature.place(x=0,y=450)

        # minimum temperature
        mintemp=Label(self,text="MINIMUM TEMPERATURE: ",width=0,bg="black",fg="orange",font=("bold,15"))
        mintemp.place(x=0,y=500)

        #gets minimum temperature
        temperature=Label(self,text="...",width=0,bg='black',font=("Helvetica",15),fg='orange')
        temperature.place(x=0,y=550)

        # description
        self.des=Label(self,text="DESCRIPTION: ",bg='black',fg='orange',font=("bold,15"))
        self.des.place(x=0,y=600)

        self.description=Label(self,text="...", width=24,bg='white',font=("bold,17"),fg="black")
        self.description.place(x=230,y=600)

        # search button
        self.button=Button(self, text="Search",bg="black",fg='white',font=("bold,12"))
        self.button["command"] = self.main
        self.button.place(x=85,y=80)

    def main(self):
        city_name:str = self.text_box.get(1.0, END)
        city_obj = CurrentCity(city_name, test=False)

        if city_obj.cod == "404": messagebox.showerror("Error","City not found")

        self.location['text'] = city_obj.name

        self.des['text'] = city_obj.weather['main']
        self.des['font'] = ('calibri',20,'bold')

        self.description['text'] = city_obj.weather['description']
        self.description['font'] = ('calibri',20,'bold')

        self.temperature['text'] = city_obj.temperature
        self.temperature['font'] = ('calibri',15,'bold')

        self.humidity['text'] = city_obj.humidity
        self.humidity['font'] = ('calibri',15,'bold')

        self.pressure['text'] = city_obj.pressure
        self.pressure['font'] = ('calibri',15,'bold')


if __name__ == '__main__':
    weather = Weather()
    weather.mainloop()
        