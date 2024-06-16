Хранение ключей и других конфиденциальных данных в коде небезопасно. Существует несколько способов безопасного хранения этих данных, 
чтобы их можно было использовать в коде, но не показывать при демонстрации или публикации кода.

### 1. Использование переменных окружения

Один из самых популярных и безопасных способов хранения конфиденциальных данных — это использование переменных окружения.

**Шаги:**

1. Создайте файл `.env` в корневой директории вашего проекта.
  
    ```plaintext
    TELEGRAM_API_TOKEN=your_telegram_api_token
    GIPHY_API_KEY=your_giphy_api_key
    ```

2. Установите библиотеку `python-dotenv` для загрузки переменных окружения из `.env` файла.

    ```sh
    pip install python-dotenv
    ```

3. Обновите свой код для использования переменных окружения.

    ```python
    import telebot
    import requests
    import os
    from dotenv import load_dotenv

    # Загрузите переменные окружения из файла .env
    load_dotenv()

    TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
    GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')

    bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

    def get_random_gif():
        url = f'http://api.giphy.com/v1/gifs/random?api_key={GIPHY_API_KEY}'
        response = requests.get(url)
        data = response.json()
        gif_url = data['data']['images']['original']['url']
        return gif_url

    @bot.message_handler(func=lambda message: True)
    def send_random_gif(message):
        gif_url = get_random_gif()
        bot.send_animation(message.chat.id, gif_url)

    if __name__ == '__main__':
        bot.polling()
    ```

4. Добавьте файл `.env` в `.gitignore`, чтобы он не был закрыт в вашем репозитории.

    ```plaintext
    .env
    ```

### 2. Использование конфигурационных файлов

Можно также использовать конфигурационные файлы, которые не включены в репозиторий. Например, файл `config.py` или `config.json`, который будет игнорироваться в `.gitignore`.

**Шаги:**

1. Создайте файл `config.py`:

    ```python
    TELEGRAM_API_TOKEN = 'your_telegram_api_token'
    GIPHY_API_KEY = 'your_giphy_api_key'
    ```

2. Обновите `.gitignore`, чтобы исключить `config.py`:

    ```plaintext
    config.py
    ```

3. Обновите свой код для импорта конфигурации:

    ```python
    import telebot
    import requests
    import os
    import config

    TELEGRAM_API_TOKEN = config.TELEGRAM_API_TOKEN
    GIPHY_API_KEY = config.GIPHY_API_KEY

    bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

    def get_random_gif():
        url = f'http://api.giphy.com/v1/gifs/random?api_key={GIPHY_API_KEY}'
        response = requests.get(url)
        data = response.json()
        gif_url = data['data']['images']['original']['url']
        return gif_url

    @bot.message_handler(func=lambda message: True)
    def send_random_gif(message):
        gif_url = get_random_gif()
        bot.send_animation(message.chat.id, gif_url)

    if __name__ == '__main__':
        bot.polling()
    ```

Оба подхода обеспечивают безопасное хранение ключей и упрощают совместную работу с кодом без риска утечки конфиденциальной информации.
