import requests

url = "https://cdn.pixabay.com/photo/2020/05/12/17/04/wind-turbine-5163993_960_720.jpg"

r = requests.get(url)
with open("wind-turbine.jpg", "wb") as f:
    f.write(r.content)