import csv

with open('parsed_data.csv', 'r', encoding='utf-8') as file, open('data\\cleaned_prices.csv', 'w', newline='', encoding='utf-8') as clean_file:
    reader = csv.reader(file)
    writer = csv.writer(clean_file)
    writer.writerow(['Price'])
    for row in reader:
        cleaned_row = int(row['Price'].replace('руб.', '').replace(' ', ''))
        writer.writerow([cleaned_row])
