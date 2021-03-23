import requests
from bs4 import BeautifulSoup    #  internetdan Rasm kuchirish



HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}


def clubname(n):
    l = []
    for i in range(1, n + 1):
        url_for_club_name = f'https://eplmanager.com/ru/widgets/player-list?page={i}'
        texts = requests.get(url_for_club_name, headers=HEADERS)
        print(texts)
        soup = BeautifulSoup(texts.text, 'lxml')
        soup1 = soup.findAll('td', class_="text-center")
        for i in soup1:
            c = i.text.strip()
            if c.isalpha() and c not in l:
                l.append(c)

    return l


def clubImages(cln):
    for i in cln:
        g = f'goalkeeper shirt {i}'
        c = f'club shirt {i}'
        url_for_image = f'https://static.eplmanager.com/static/design/shirts/retina/{i}.png'
        goalkeeper_url_for_image = f'https://static.eplmanager.com/static/design/shirts/goalkeepers/retina/{i}.png'
        response_image = requests.get(url_for_image).content
        response_goalkeeper = requests.get(goalkeeper_url_for_image).content
        with open(f'/home/alex/Desktop/for_image/{g}.png', 'wb') as f:
            f.write(response_goalkeeper)
            print('ok for goalkeeper')
        with open(f'/home/alex/Desktop/for_image/{c}.png', 'wb') as f:
            f.write(response_image)
            print('ok for club')



def natija():
    club_name = clubname(int(input('Necha sahifa: ')))
    clubImages(club_name)

    print('fine')

natija()