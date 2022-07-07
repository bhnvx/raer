import bs4
import requests


url = "https://maplestory.nexon.com/news/notice"

req = requests.get(url)
soup = req.text