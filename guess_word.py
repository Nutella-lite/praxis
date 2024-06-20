from bs4 import BeautifulSoup
import requests
from googletrans import Translator
translator = Translator()

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        english_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_word": english_word,
            "english_definition": english_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Нужно угадать слово по описанию его значения")
    while True:
        lang = input("Выберите язык: 1 - английский, 2 - русский: ")
        word_dict = get_english_words()
        word = word_dict["english_word"]
        definition = word_dict["english_definition"]
        if lang == "2":
            word = translator.translate(word, dest="ru").text
            definition = translator.translate(definition, dest="ru").text

        print(f"Значение слова:  {definition}")
        user_guess = input("Ваш вариант слова: ")
        if user_guess == word:
            print("Бинго!")
        else:
            print(f"Не совсем. Точный ответ - {word}")

        go_on = input("Хотите еще попробовать? (y/n): ")
        if go_on != "y":
            print("Спасибо за игру!")
            break

word_game()