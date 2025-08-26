from bs4 import BeautifulSoup
from googletrans import Translator
import requests

def get_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        word_en = soup.find("div", id ="random_word").text.strip()
        word_definition_en = soup.find("div", id="random_word_definition").text.strip()

        translator = Translator()
        word_definition_ru = translator.translate(word_definition_en, src="en", dest="ru").text
        word_ru = translator.translate(word_en, src="en", dest="ru").text

        return {
            "word_en": word_en,
            "word_definition_en": word_definition_en,
            "word_ru": word_ru,
            "word_definition_ru": word_definition_ru
        }
    except:
        return "Error"

def word_game():
    print("Добро пожаловать")
    while True:
        word_dict = get_words()
        word = word_dict["word_ru"]
        word_en = word_dict["word_en"]
        word_definition = word_dict["word_definition_ru"]
        word_definition_en = word_dict["word_definition_en"]


        print(f"Значение слова(русский) - {word_definition}")
        print(f"Значение слова(английский)- {word_definition_en}")
        user = input("Введите слово: ")
        if user == word:
            print("Правильно")
        else:
            print(f"Неправильно, Правильное слово(русский) - {word}")
            print(f"Неправильно, Правильное слово(английский) - {word_en}")

        play_again = input("Хотите сыграть еще? (да/нет): ")
        if play_again.lower() != "да":
            print("Спасибо за игру")
            break

word_game()