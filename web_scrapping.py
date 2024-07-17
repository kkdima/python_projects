from os import name
import requests
from bs4 import BeautifulSoup

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

table_element = soup.find(
    "table", class_="tableVariant1")

if table_element is not None:
    for user in table_element.find_all("tr")[1:]:
        name = user.find_all("td")[1].text.replace("\n", "")
        followers = user.find_all("td")[2].text.replace("million", "")
        print(f"{name}: {followers}")
