import requests

try:
    from . import OPENW_API_KEY
    from .conversion import *
except ImportError:
    from open_weather import  OPENW_API_KEY
    from open_weather.conversion import *
    print("IMPORT ERROR")


class CurrentCity:
    """OpenWeather API framework for getting the current weather information of a city.
    Example use,
    >>> kolkata = CurrentCity('kolkata')
    >>> kolkata.coord
    {"lon":88.3697,"lat":22.5697}
    >>> kolkata.wind
    {"speed":2.06, "deg":160}
    >>> kolkata.humidity
    89

    NOTE: For testing and developing do not use the api link directly. Instead use the sample data set given below.
    """    
    def __init__(self, name:str, test=True):
        if " " in name:
            name = name.replace(" ", "%20")
            
        if test:
            self.response = {"coord":{"lon":-74.006,"lat":40.7143},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
            "base":"stations","main":{"temp":297.09,"feels_like":297.5,"temp_min":294.9,"temp_max":298.8,"pressure":1017,"humidity":75},
            "visibility":10000,"wind":{"speed":4.12,"deg":250},"clouds":{"all":1},"dt":1631536477,"sys":{"type":1,"id":4610,"country":"US",
            "sunrise":1631529303,"sunset":1631574537},"timezone":-14400,"id":5128581,"name":"New York","cod":200}
        else:
            API_LINK = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={OPENW_API_KEY}"
            self.response = requests.get(API_LINK).json()

    @property
    def name(self) -> str:
        return self.response["name"]

    @property
    def visibility(self) -> int:
        return self.response["visibility"]

    @property
    def coord(self) -> dict:
        """Returns coordinates dictionary of the input city

        Returns:
            dict: {'lon': 88.3697, 'lat': 22.5697}
        """        
        return self.response["coord"]

    @property
    def weather(self) -> dict:
        """Returns weather dictionary of the input city

        Returns:
            dict: {'main': 'Clear', 'description': 'clear sky'}
        """        
        temp:dict = self.response["weather"][0]
        main = temp["main"]
        description = temp["description"]

        return {"main":main, "description":description}


    # MAIN CATEGORY START
    @property
    def main(self) -> dict:
        return self.response["main"]

    @property
    def temperature(self, round_digit=2) -> float:
        return to_celsius(self.main["temp"], round_digit)

    @property
    def feels_like(self, round_digit=2) -> float:
        return to_celsius(self.main["feels_like"], round_digit)

    @property
    def temp_min(self, round_digit=2) -> float:
        return to_celsius(self.main["temp_min"], round_digit)

    @property
    def temp_max(self, round_digit=2) -> float:
        return to_celsius(self.main["temp_max"], round_digit)
    
    @property
    def pressure(self) -> float:
        return self.main["pressure"]

    @property
    def humidity(self) -> float:
        return self.main["humidity"]
    #MAIN CATEGORY END
    
    @property
    def wind(self) -> dict:
        """Returns wind direction and speed in km/h

        Returns:
            dict: {"speed":2.06, "deg":160}
        """        
        return self.response["wind"]

    @property
    def cod(self) -> int:
        """Should return 200
        """
        return self.response["cod"]

    @property
    def icon_url(self) -> str:
        temp:dict = self.response["weather"][0]
        return f"https://openweathermap.org/img/w/{temp['icon']}"

    def __str__(self) -> str:
        """Usage:
        >>> paris = CurrentCity('Paris')
        >>> str(paris)
        """  

        return \
        f"""
        Name: {self.name}
        Coordinates: {self.coord}
        Weather: {self.weather}
        Temperature: {self.temperature}
        Pressure: {self.pressure}
        Wind: {self.wind}
        """