from bs4 import BeautifulSoup as bs
from typing import List, Dict
import requests


def _generate_url(num: int) -> str:
    url = f"https://maplestory.nexon.com/news/notice?page={num}"
    return url


def _get_page(url: str) -> bs:
    req = requests.get(url)
    soup = bs(req.text, 'html.parser')
    return soup


def events_of_get_contents(num: int) -> List[str]:
    url = _generate_url(num)
    page = _get_page(url)
    raw = page.find_all("span")
    urls = page.find_all("a")[99:109]

    res = []
    url = []

    for r in raw[18:28]:
        res.append(r.text)

    for u in urls:
        url.append("https://maplestory.nexon.com"+u.get('href'))

    return res, url


def create_events_dict(num: int) -> Dict:
    events = dict()
    items, url = events_of_get_contents(num)

    for i in range(len(items)):
        events[f"item{i}"] = {"notice": items[i], "url": url[i]}

    return events
