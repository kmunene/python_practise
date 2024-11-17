from bs4 import BeautifulSoup as b
import requests

url = "https://odibets.com/odileague"

response = requests.get(url)
print(response.status_code)

soup = b(response.text, "html.parser")
a = soup.find_all("div", class_="t")
for week in a:
  print(week.text.strip())
