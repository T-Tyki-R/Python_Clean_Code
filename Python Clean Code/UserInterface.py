from WeatherDataFetcher import WeatherData
from DataParser import DataParser

class UserInterface:
    def display_weather(self, city):
    # Function to display the basic weather forecast for a city
        data = WeatherData.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report =DataParser.parse_weather_data()
            print(weather_report)

    def get_detailed_forecast(self, city):
        data = WeatherData.fetch_weather_data(city)
        return DataParser.parse_weather_data(data)

    def main(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(forecast)


