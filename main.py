from tkinter import * 
from tkinter import messagebox
from datetime import datetime 
import tkinter as tk
from PIL import ImageTk, Image

from open_weather.current import CurrentCity

class Weather(tk.Tk):

    @property
    def font(self):
        return ('calibri',10,'bold')
    
    def __init__(self):
        super().__init__()

        # configure the root window
        self.geometry('500x300')
        self.title("WEATHER REPORT")
        self.maxsize(500,300)
        self.minsize(500,300)

        # add header
        self.header=Label(self, width=100, height=2, bg="#00274c")
        self.header.place(x=0,y=0)

        # date label
        self.date=Label(self, text=datetime.now().date(), bg="#00274c", fg="red", font=self.font)
        self.date.place(x=400,y=5)

        # heading label
        self.heading=Label(self, text="Weather Report", bg="#00274c", fg="white", font=self.font)
        self.heading.place(x=180,y=5)

        self.location=Label(self, text="NA-/", bg="#00274c", fg="blue", font=self.font)

        # icon.png
        # self.image1=ImageTk.PhotoImage(Image.open('.\images\icon.png'))
        # self.image1=Label(self, image=self.image1)
        # self.image1.place(x=20,y=40)

        # city or country name label
        self.name=Label(self, text="City or Country Name", fg="#00274c", font=self.font)
        self.name.place(x=140,y=45)

        # 
        self.loc=Text(self, width=25, height=2)
        self.loc.place(x=140,y=70)


        # line1 label
        self.line1=Label(self, bg="#00274c", width=20, height=0)
        self.line1.place(x=0,y=150)
        self.line2=Label(self, bg="#00274c", width=20, height=0)
        self.line2.place(x=360,y=150)

        # report label
        self.report=Label(self, text="Weather Report", bg="#00274c", fg="white" ,font=self.font, padx=10)
        self.report.place(x=180,y=150)

        # icon2.png
        # self.image2=ImageTk.PhotoImage(Image.open('.\images\icon2.png'))
        # self.image2=Label(self, image=self.image2)
        # self.image2.place(x=90,y=180)

        # weather
        self.weather=Label(self, text="NA/-", fg="#00274c", font=self.font)
        self.weather.place(x=90,y=230)

        # icon3.png
        # self.image3=ImageTk.PhotoImage(Image.open('.\images\icon3.png'))
        # self.image3=Label(self, image=self.image3)
        # self.image3.place(x=200,y=180)

        # temperature
        self.temperature=Label(self, text='NA/-',fg="#00274c",font=self.font)
        self.temperature.place(x=200,y=230)

        # icon4.png
        # self.image4=ImageTk.PhotoImage(Image.open('.\images\icon4.png'))
        # self.image4=Label(self, image=self.image3)
        # self.image4.place(x=310,y=230)


        # humidity
        self.humidity=Label(self, text="NA/-", fg="#00274c", font=self.font)
        self.humidity.place(x=310,y=230)

        # icon5.png
        # self.image5=ImageTk.PhotoImage(Image.open('.\images\icon5.png'))
        # self.image5=Label(self, image=self.image5)
        # self.image5.place(x=380,y=180)

        # pressure
        self.pressure=Label(self, text="NA/-",fg="#00274c",font=self.font)
        self.pressure.place(x=380,y=230)

        # search button
        self.button=Button(self, text="Search",bg="#00274c",fg='white',font=self.font)
        self.button["command"] = self.main
        self.button.place(x=350,y=73)

    def main(self):
        city_name:str = self.loc.get(1.0, END)
        city_obj = CurrentCity(city_name, test=False)

        if city_obj.cod == "404":
            messagebox.showerror("Error","City not found")

        self.location['text'] = city_obj.name

        self.weather['text'] = city_obj.weather['main']
        self.weather['font'] = ('calibri',20,'bold')

        self.temperature['text'] = city_obj.temperature
        self.temperature['font'] = ('calibri',15,'bold')

        self.humidity['text'] = city_obj.humidity
        self.humidity['font'] = ('calibri',15,'bold')

        self.pressure['text'] = city_obj.pressure
        self.pressure['font'] = ('calibri',15,'bold')


if __name__ == '__main__':
    weather = Weather()
    weather.mainloop()
        