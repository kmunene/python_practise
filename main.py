from bs4 import BeautifulSoup
import requests
import json

main_page_url = "https://jumia.co.ke/"

main_page_data = requests.get(main_page_url)

if main_page_data.status_code != 200:
    print("no bots mofo")

main_page_soup = BeautifulSoup(main_page_data.text, 'html.parser')

mini_site_urls = [a['href'] for a in main_page_soup.find_all('a', href=True)]

for link in mini_site_urls:
    print(link)
