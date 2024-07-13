from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

def get_parsed_items(browser):
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'wYUX2'))
    )
    items = browser.find_elements(By.CLASS_NAME, 'wYUX2')
    parsed_data = []
    for item in items:
        try:
            name = item.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
            price = item.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text
            link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
            parsed_data.append([name, price, link])
        except Exception as e:
            print(f'Error parsing item: {e}')
    return parsed_data

def main():
    browser = webdriver.Firefox()
    url = 'https://www.divan.ru/category/dekor'
    browser.get(url)

    all_data = []

    try:
        while True:
            parsed_data = get_parsed_items(browser)
            all_data.extend(parsed_data)

            next_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.PaginationLink'))
            )
            next_button.click()
    except Exception as e:
        print('No more pages or error:', e)
    finally:
        browser.quit()

    with open('parsed_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(['Name', 'Price', 'Link'])
        writer.writerows(all_data)

if __name__ == "__main__":
    main()
