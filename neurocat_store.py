class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def update_item(self, item_name, item_price):
        self.items[item_name] = item_price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

class Stores:
    def __init__(self):
        self.stores = {}

    def add_store(self, name, address):
        if address not in self.stores:
            self.stores[address] = Store(name, address)

    def add_item_to_store(self, store_address, item_name, item_price):
        if store_address in self.stores:
            self.stores[store_address].update_item(item_name, item_price)
        else:
            print("Магазин не найден")

    def remove_item_from_store(self, store_address, item_name):
        if store_address in self.stores:
            self.stores[store_address].remove_item(item_name)
        else:
            print("Магазин не найден")

    def get_item_prices(self, item_name):
        for store in self.stores.values():
            print(f"Магазин '{store.name}' по адресу: {store.address}")
            price = store.get_item_price(item_name)
            if price is not None:
                print(f"Цена: {price}")
            else:
                print("Товар не найден.")

    def show_stores(self):
        if not self.stores:
            print("Магазинов пока нет")
        else:
            for i, store in enumerate(self.stores.values(), 1):
                print(f"{i}) '{store.name}' по адресу: {store.address}")

    def get_item_range(self, store_address):
        if store_address in self.stores:
            print(self.stores[store_address].items)
        else:
            print("Магазин не найден")

my_stores = Stores()
running = True
while running:
    action = int(input("Выберите действие: "
                       "\n1 - показать список магазинов "
                       "\n2 - добавить товары в магазин "
                       "\n3 - удалить товары из магазина "
                       "\n4 - получить цены товара в магазинах "
                       "\n5 - обновить цену товара в магазине "
                       "\n6 - получить ассортимент товаров в магазине "
                       "\n7 - добавить магазин "
                       "\n8 - выход из программы \n"))
    if action == 1:
        my_stores.show_stores()
    elif action == 2 or action == 5:
        store_address = input("Введите адрес магазина: ")
        item_name = input("Введите название товара: ")
        item_price = float(input("Введите цену товара: "))
        my_stores.add_item_to_store(store_address, item_name, item_price)
    elif action == 3:
        store_address = input("Введите адрес магазина: ")
        item_name = input("Введите название товара: ")
        my_stores.remove_item_from_store(store_address, item_name)
    elif action == 4:
        item_name = input("Введите название товара: ")
        my_stores.get_item_prices(item_name)
    elif action == 6:
        store_address = input("Введите адрес магазина: ")
        my_stores.get_item_range(store_address)
    elif action == 7:
        name = input("Введите название магазина: ")
        address = input("Введите адрес магазина: ")
        my_stores.add_store(name, address)
    elif action == 8:
        running = False