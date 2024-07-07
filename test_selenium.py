from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard

def get_page(browser, seek):
    """Загружает страницу поиска и переходит на первую найденную страницу."""
    try:
        search_box = browser.find_element(By.ID, "searchInput")
        search_box.clear()
        search_box.send_keys(seek)
        search_box.send_keys(Keys.RETURN)

        # Ожидание результатов поиска и переход на первую найденную страницу
        first_result = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul.mw-search-results li a"))
        )
        first_result.click()

        # Ожидание загрузки первой найденной страницы
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "firstHeading"))
        )
    except Exception as e:
        print(f"Ошибка при загрузке страницы: {e}")
        return None
    return browser.page_source

def get_items(browser):
    """Возвращает словарь ссылок на статьи с текущей страницы."""
    items_dict = {}
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "div"))
        )
        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl in ["hatnote navigation-not-searchable", "mw-heading mw-heading2"]:
                try:
                    anchor = element.find_element(By.TAG_NAME, "a")
                    title = anchor.get_attribute("title")
                    href = anchor.get_attribute("href")
                    if title and href:
                        items_dict[title] = href
                except Exception as e:
                    print(f"Ошибка при обработке элемента: {e}")
        print(f"Найдено ссылок: {len(items_dict)}")
    except Exception as e:
        print(f"Ошибка при получении элементов: {e}")
    return items_dict

def print_paragraphs(browser):
    """Выводит параграфы текущей страницы по одному за нажатие Enter."""
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    index = 0
    while index < len(paragraphs):
        paragraph = paragraphs[index]
        if paragraph.text.strip():
            print(paragraph.text)
            print("Enter - для продолжения, Esc - для выбора действия")
            while True:
                if keyboard.is_pressed('enter'):
                    index += 1
                    break
                elif keyboard.is_pressed('esc'):
                    return

def main():
    print("Добро пожаловать в сервис поиска по Википедии!")
    browser = webdriver.Firefox()
    try:
        browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
        assert "Википедия" in browser.title

        while True:
            seek = input("Что будем искать? ")
            if get_page(browser, seek) is None:
                continue

            while True:
                items_dict = get_items(browser)
                if items_dict:
                    print("Вот какие статьи есть на найденной странице: ")
                    for key in items_dict:
                        print(key)
                else:
                    print("Статьи не найдены")

                choice = input("\n\nВыберите действие: \n1 - выводить параграфы всей страницы по enter \n2 - перейти на связанную статью \n3 - выйти из программы\n")
                if choice == '1':
                    print_paragraphs(browser)
                elif choice == '2':
                    title = input("Введите название статьи, на которую хотите перейти: ")
                    if title in items_dict:
                        try:
                            browser.get(items_dict[title])
                            WebDriverWait(browser, 10).until(
                                EC.presence_of_element_located((By.ID, "firstHeading"))
                            )
                        except Exception as e:
                            print(f"Ошибка при загрузке страницы: {e}")
                    else:
                        print("Статья не найдена. Попробуйте еще раз.")
                elif choice == '3':
                    return
                else:
                    print("Некорректный выбор. Пожалуйста, выберите действие снова.")
    finally:
        browser.quit()

if __name__ == "__main__":
    main()
