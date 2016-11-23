# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys

from login import login

INDEX_URL = 'https://www.v2ex.com/'


def daily(username, password):
    s = login(INDEX_URL + 'signin', username, password)
    r = s.get(INDEX_URL + 'mission/daily')
    soup = BeautifulSoup(r.text, 'html.parser')
    url = soup.find('input', attrs={'type': 'button'})['onclick'][18: -2]
    s.get(INDEX_URL + url)

if __name__ == "__main__":
    daily(sys.argv[1], sys.argv[2])
