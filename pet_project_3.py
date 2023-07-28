import requests
from bs4 import BeautifulSoup
x = 0
with open('phohe.txt', 'w', encoding='utf-8') as nomer:

    for i in range(1,1000):
        url = f'https://berkat.ru/board?page={i}'

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find_all('div', class_='board_list_footer_left')

        for i in data:
            x += 1
            spans = i.find_all('span', class_='')
            phone = i.find('a', class_='get_phone_style').text
            if len(spans) >= 5:
                name = spans[7].text
                name = str("".join(name.split()))
                nomer.write(name + '}' + phone + '\n')