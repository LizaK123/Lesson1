# import urllib.request
#
# opener = urllib.request.build_opener()
# response = opener.open("https://httpbin.org/get")
# print(response())

import requests
response = requests.get("https://httpbin.org/get")
print(response.content)
print(type(response.text))

respone = requests.post("https://httpbin.org/post", data="Yura")
print(response.text)
response = requests.post("https://httpbin.org/post", headers={"h1", "Yura"})

import requests
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                print(parse_elem_2)

from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"
soup = BeautifulSoup(response.content,"html.parser")
quotes = soup.find_all("span", {"class" : "text"})


for quote in quotes:
    print(quote.text)
    print(type(quote.text))
