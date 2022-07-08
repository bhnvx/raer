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


def events_of_get_content(num: int) -> List[str]:
    url = _generate_url(num)
    page = _get_page(url)
    raw = page.find_all("span")

    res = []

    for r in raw:
        res.append(r.text)

    return res[18:28]


def create_events_dict(num: int) -> Dict:
    events = dict()
    items = events_of_get_content(num)

    for i in range(len(items)):
        events[f"item{i}"] = items[i]

    return events
