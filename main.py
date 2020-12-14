from bs4 import BeautifulSoup
import requests


date = input("Which date do you want the machine to get music from? YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, "html.parser")

all_elements = soup.find_all(name="span", class_="chart-element__information")

chart = []

for elem in all_elements:
    song = elem.find(class_="chart-element__information__song text--truncate color--primary").getText()
    artist = elem.find(class_="chart-element__information__artist text--truncate color--secondary").getText()
    chart.append(f"{song},{artist}")