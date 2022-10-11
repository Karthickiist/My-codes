import requests
api_key='dfb45fe9a8c9a1a22dd4c1a0709089c8'

data=requests.get(url='https://api.openweathermap.org/data/2.5/weather?lat=43.653225&lon=-79.383186&appid=dfb45fe9a8c9a1a22dd4c1a0709089c8')
print(data.json())
