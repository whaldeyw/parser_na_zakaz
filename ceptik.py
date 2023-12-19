import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

with open('ссылки.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    with open('ceptic.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        print('Загружаю данные')

        writer.writerow(
            (
                'Название',
                'Картинка',
                'Цена',
                'ав',
                'Монтаж',
                'Оплата',
                'Бренд',
                'Проживание',
                'Высота'

            )
        )

        for line in reader:
            url = dict(line)['Ссылки']
            headers = {
                "Accept": "*/*",
                "User-Agent": "UserAgent().chrome"
            }

            r = requests.get(url, headers=headers)
            src = r.text

            soup = BeautifulSoup(src, 'lxml')
            name = soup.find(class_='h2').text
            src = soup.find(class_='product-card-top-info').find('a').get('href')
            ikonca = requests.get(f'https://septiki-topas.su/{src}').content
            with open('i.jpg', 'wb') as file:
                file.write(ikonca)

            price = soup.find(class_='product-price').text
            delivery = soup.find(class_='desc').text
            montag = soup.find_all(class_='line')[4].find(class_='desc').text
            oplata = soup.find_all(class_='line')[5].find(class_='desc').text
            brend = soup.find_all(class_='cont')[0].find(class_='desc').text
            rezidence = soup.find_all(class_='cont')[1].find(class_='desc').text
            height  =  soup.find_all(class_='cont')[3].find(class_='desc').text

            print(f'{name}\n{ikonca}\n{price}\n{delivery}\n{montag}\n{oplata}\n{brend}\n{rezidence}\n{height}')

            with open('ceptic.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)

                writer.writerow(
                    (
                        name,
                        open('i.jpg'),
                        price,
                        delivery,
                        montag,
                        oplata,
                        brend,
                        rezidence,
                        height
                    )
                )