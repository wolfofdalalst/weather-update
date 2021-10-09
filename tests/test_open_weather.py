import unittest
from open_weather.current import CurrentCity
from open_weather.conversion import to_celcius

class TestOpenWeather(unittest.TestCase):

    def setUp(self) -> None:
        test_city = ["Kolkata", "Paris", "Berlin"]
        self.test_city_list = []
        for city in test_city:
            self.test_city_list.append(CurrentCity(city, test=False))

    def test_cod(self):
        for city in self.test_city_list:
            self.assertEqual(city.cod, 200, "SERVER ERROR: Cod should be 200")

    def test_temp(self):
        for city in self.test_city_list:
            temp = city.temperature
            self.assertIsInstance(temp, float, "Temperature should be float")
            self.assertLessEqual(temp, 60, "Temp <= 60")
            self.assertGreaterEqual(temp, -90, "Temp >= -90")

    #TODO: Add test function to check .\open_weather\conversion.py

    def test_humidity(self):
        for city in self.test_city_list:
            humidity = city.humidity
            self.assertLessEqual(humidity, 100, "Humidity <= 100")
            self.assertGreaterEqual(humidity, 0, "Humidity >= 0")

if __name__ == "__main__":
    unittest.main()