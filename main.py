from bs4 import BeautifulSoup
import requests

page = 1

while page < 106:

    url = f'https://www.libok.net/writer/66/kniga/14306/azimov_ayzek/akademiya_osnovanie_-_1_prelyudiya_k_osnovaniyu_prelyudiya_k_akademii/read/{page}'

    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    block_text = soup.find('div', class_='cblock')

    for a in block_text.find_all('a'):
        a.extract()

    text = block_text.text

    with open('osnovsnie_book.txt', 'a', encoding='utf-8') as file:
        file.write(text.strip())

    print(f'записал страницу {page}')
    page += 1