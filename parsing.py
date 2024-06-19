from bs4 import BeautifulSoup
import requests
import random

all_authors = set()  # Используем множество для отслеживания уникальных авторов
author_list = []  # Используем список для индексируемого хранения авторов
all_quotes = dict()
url = "http://quotes.toscrape.com/"

while url:
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # Получение цитат и авторов
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    for i in range(len(quotes)):
        author_name = authors[i].text
        quote_text = quotes[i].text
        if author_name not in all_authors:
            all_authors.add(author_name)
            author_list.append(author_name)
        all_quotes[quote_text] = author_name

    # Поиск ссылки на следующую страницу
    next_button = soup.find("li", class_="next")
    if next_button:
        next_page_url = next_button.find("a")["href"]
        url = "http://quotes.toscrape.com" + next_page_url
    else:
        url = None

author_list = sorted(author_list)
print('Вот список авторов:')
for i, author in enumerate(author_list):
    print(i, ' - ', author)
print("Кому из них принадлежит цитата?")
go_on = 'y'
while go_on == 'y':
    random_quote = random.choice(list(all_quotes.keys()))
    print(random_quote)
    user_choice = int(input('Введите номер автора в списке:  '))
    if author_list[user_choice] == all_quotes[random_quote]:
        print('Вы угадали!')
    else:
        print(f'Вы не угадали. Автор слов - {all_quotes[random_quote]}')
    go_on = input('Хотите еще раз? (y/n):  ')
