from WeatherDataFetcher import WeatherData
from DataParser import DataParser

class UserInterface:
    def __init__(self):
        self.weather_fetcher = WeatherData()
        self.data_parser = DataParser()

    def display_basic_weather(self, city):
        data = self.weather_fetcher.fetch_weather_data(city)
        if not data:
            return f"Weather data not available for {city}"
        else:
            return self.data_parser.parse_weather_data(data)

    def get_detailed_forecast(self, city):
        data = self.weather_fetcher.fetch_weather_data(city)
        return self.data_parser.parse_weather_data(data)

    def main(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_basic_weather(city)
            print(forecast)


