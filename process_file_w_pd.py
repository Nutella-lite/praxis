import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('data\\parsed_prices.csv', encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv('data\\parsed_prices.csv', encoding='cp1251')

prices = df['Price'].str.replace(r'[^0-9]', '', regex=True).astype(int)
print(f"Количество цен: {len(prices)}")
print(f"Средняя цена: {prices.mean():.2f}")

plt.hist(prices, bins=40, edgecolor='black')
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.show()

clean_df = pd.DataFrame({'Price': prices})
clean_df.to_csv('data\\cleaned_prices.csv', index=False)