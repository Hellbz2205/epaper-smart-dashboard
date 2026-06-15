import requests

def get_weather(lat, lon, cfg):
    key = cfg["weather"]["api_key"]

    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": key,
        "units": "metric",
        "lang": "de"
    }

    try:
        r = requests.get(url, params=params, timeout=5)
        data = r.json()["list"][:4]

        forecast = []
        for f in data:
            forecast.append({
                "time": f["dt_txt"][11:16],
                "temp": f["main"]["temp"],
                "desc": f["weather"][0]["main"]
            })

        return {
            "temp": data[0]["main"]["temp"],
            "humidity": data[0]["main"]["humidity"],
            "desc": data[0]["weather"][0]["description"],
            "forecast": forecast
        }

    except Exception as e:
        return {"error": str(e)}