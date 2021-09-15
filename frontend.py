from tkinter import *    #importing tkinter module 
from datetime import datetime   #importing datetime module   
import tkinter as tk
from PIL import ImageTk,Image
import requests
from tkinter import messagebox
class Weather():
    def weather_report(self):
                
                self.url = "http://api.openweathermap.org/data/2.5/weather?q="
                self.cityname =  self.loc.get(1.0,END)
                self.api_key="955b33778e339118d99448d78cb46bab"
                self.data = requests.get(self.url+self.cityname+'&appid='+self.api_key).json()
                if self.data['cod']=='404':
                    messagebox.showerror("Error","City not found")
                else:
                    self.location['text']=self.data['name']
                    self.c=self.data['main']['temp_max']-273.15
                    self.f=self.c*9/5+32
                    self.weather['text']=self.data['weather'][0]['main']
                    self.weather['font']=('calibri',20,'bold')
                    self.temperature['text']=f'{self.c}C\n{self.f}F'
                    self.temperature['font']=('calibri',15,'bold')
                    self.humidity['text']=self.data['main']['humidity']
                    self.humidity['font']=('calibri',15,'bold')
                    self.pressure['text']=self.data['main']['pressure']
                    self.pressure['font']=('calibri',15,'bold')




    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry('500x300')
        self.window.title("WEATHER REPORT")
        self.window.maxsize(500,300)
        self.window.minsize(500,300)
    
        self.header=Label(self.window,width=100,height=2,bg="#00274c")
        self.header.place(x=0,y=0)

        self.font=('calibri',10,'bold')

        self.date=Label(self.window,text=datetime.now().date(),bg="#00274c",fg="red",font=self.font)
        self.date.place(x=400,y=5)

        self.heading=Label(self.window,text="Weather Report",bg="#00274c",fg="white",font=self.font)
        self.heading.place(x=180,y=5)

        self.location=Label(self.window,text="NA-/",bg="#00274c",fg="blue",font=self.font)

        self.image1=ImageTk.PhotoImage(Image.open('icon.png'))
        self.image1=Label(self.window,image=self.image1)
        self.image1.place(x=20,y=40)

        self.name=Label(self.window,text="City or Country Name",fg="#00274c",font=self.font)
        self.name.place(x=140,y=45)

        self.loc=Text(self.window,width=25,height=2)
        self.loc.place(x=140,y=70)

        self.button=Button(self.window,text="Search",bg="#00274c",fg='white',font=self.font)
        self.button.place(x=350,y=73)

        self.line1=Label(self.window,bg="#00274c",width=20,height=0)
        self.line1.place(x=0,y=150)
        self.line2=Label(self.window,bg="#00274c",width=20,height=0)
        self.line2.place(x=360,y=150)

        self.report=Label(self.window,text="Weather Report",bg="#00274c",fg="white",font=self.font,padx=10)
        self.report.place(x=180,y=150)

        self.image2=ImageTk.PhotoImage(Image.open('icon2.png'))
        self.image2=Label(self.window,image=self.image2)
        self.image2.place(x=90,y=180)
        self.weather=Label(self.window,text="NA/-",fg="#00274c",font=self.font)
        self.weather.place(x=90,y=230)

        self.image3=ImageTk.PhotoImage(Image.open('icon3.png'))
        self.image3=Label(self.window,image=self.image3)
        self.image3.place(x=200,y=180)
        self.temperature=Label(self.window,text='NA/-',fg="#00274c",font=self.font)
        self.temperature.place(x=200,y=230)

        self.image4=ImageTk.PhotoImage(Image.open('icon4.png'))
        self.image4=Label(self.window,image=self.image3)
        self.image4.place(x=310,y=230)
        self.humidity=Label(self.window,text="NA/-",fg="#00274c",font=self.font)
        self.humidity.place(x=310,y=230)

        self.image5=ImageTk.PhotoImage(Image.open('icon5.png'))
        self.image5=Label(self.window,image=self.image5)
        self.image5.place(x=380,y=180)
        self.pressure=Label(self.window,text="NA/-",fg="#00274c",font=self.font)
        self.pressure.place(x=380,y=230)
        
        self.window.mainloop()

if __name__ == '__main__':
    Weather()
        