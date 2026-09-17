import requests

def multiply(a, b):
    return a * b

def weather(city):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "zh"
    }

    geo_response = requests.get(
        geo_url,
        params=geo_params
    )

    geo_data = geo_response.json()

    if "results" not in geo_data:
        return "没有找到这个城市"

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m"
    }

    weather_response = requests.get(
        weather_url,
        params=weather_params
    )

    weather_data = weather_response.json()

    temperature = weather_data["current"]["temperature_2m"]

    return city + "当前温度：" + str(temperature) + "°C"

def github_user(username):
    url = "https://api.github.com/users/" + username
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return "没有找到这个GitHub用户"

    name = data["name"]
    repos = data["public_repos"]
    followers = data["followers"]

    return (
        "用户名：" + str(name) +
        "，公开仓库：" + str(repos) +
        "，粉丝数：" + str(followers)
    )
