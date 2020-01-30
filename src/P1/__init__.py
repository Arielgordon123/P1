import requests

def get_weather(lat,lon):
    r = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?units=metric&lat={lat}&lon={lon}&APPID=8467817fe900c355d1fbdaf49de57912').json()
    return r['list'][0]['main']['temp']


def main():
    print("P1 call to => get weather:",get_weather(32.0853,34.7818))
if __name__ == "__main__":
    main()