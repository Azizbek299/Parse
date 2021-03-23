import requests
from bs4 import BeautifulSoup
import json

HOST = 'https://eplmanager.com/'
URL = 'https://eplmanager.com/ru/widgets/player-list?page=1'
HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}


def get_html(number):
    d = dict()
    l = []
    for i in range(1, number + 1):
        url = f'https://eplmanager.com/ru/widgets/player-list?page={i}'
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'html.parser')
        data_ = soup.findAll('a', class_='place-player')
        for i in data_:
            v = i['data-params'].split('"')
            d[v[1]] = v[3]
            # d[v[5]] = v[7]
            d[v[9]] = v[11]
            # d[v[13]] = v[15]
            d[v[17]] = v[19]
            # d[v[21]] = v[23]
            d[v[25]] = v[27]
            d[v[29]] = v[31]
            d[v[33]] = v[35]
            d[v[37]] = v[39]
            d[v[41]] = v[43]
            p = d.copy()
            l.append(p)

    with open('/home/alex/Desktop/J2.json', 'w') as f:
        json.dump(l, f)

    with open('/home/alex/Desktop/J.json', 'r') as fr:
        h = json.load(fr)
    for k in h:
        print(k)


get_html(int(input(': ')))
