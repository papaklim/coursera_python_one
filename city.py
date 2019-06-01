import requests


class WeatherForecast:

    def get_weather(self, city):
        url = "http://api.apixu.com/v1/current.json?key=c6dcbfbf4e3047f99a3162321193003&q={}".format(city)

        full_response = (requests.get(url)).json()
        needed_data = dict()
        needed_data["city"] = full_response["location"]["name"]
        needed_data["date"] = full_response["current"]["last_updated"]
        needed_data["fact_temp"] = full_response["current"]["temp_c"]
        needed_data["feeling_temp"] = full_response["current"]["feelslike_c"]
        needed_data["condition"] = full_response["current"]["condition"]["text"]
        return needed_data


class CityInfo:
        def __init__(self, city, weather_forecast=None):
            self.city = city
            self._weather_forecast = weather_forecast or WeatherForecast()

        def weather_forecast(self):
            return self._weather_forecast.get_weather(self.city)

def _main():
    spb = CityInfo("Saint Petersburg")
    msk = CityInfo("Moscow")
    lnd = CityInfo("London")
    forecast_spb = spb.weather_forecast()
    forecast_msk = msk.weather_forecast()
    forecast_lnd = lnd.weather_forecast()
    print(forecast_spb)
    print(forecast_msk)
    print(forecast_lnd)


if __name__ == "__main__":
    _main()
