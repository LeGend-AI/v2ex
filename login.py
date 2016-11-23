# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


def login(login_url, username, password, s=None):
    s = s or requests.session()
    s.headers.update({
        'referer': login_url,
    })
    r = s.get(login_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    user = soup.find('input', attrs={'class': 'sl', 'type': 'text'})['name']
    passwd = soup.find('input', attrs={'class': 'sl', 'type': 'password'})['name']
    n = soup.find('input', attrs={'name': 'next'})['value']
    o = soup.find('input', attrs={'name': 'once'})['value']
    data = {
        user: username,
        passwd: password,
        'next': n,
        'once': o,
    }
    r = s.post(login_url, data=data)
    if username not in r.text:
        return None
    return s
