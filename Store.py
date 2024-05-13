class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def update_item(self,  item_name, item_price):
        self.items[item_name] = item_price

    def remove_item(self, it_name):
        self.items.pop(it_name)

    def get_item_price(self, it_name):
        return self.items.get(it_name, None)


class Stores:
    def __init__(self):
        self.stores = []

    def add_store(self):
        n = int(input("Какое количество магазинов хотите добавить: "))
        for i in range(n):
            name = input(f"Введите название магазина: ")
            address = input(f"Введите адрес магазина: ")
            store = Store(name, address)
            self.stores.append(store)

    def add_item_to_store(self):
        store_address = input("Введите адрес магазина: ")
        store_found = False
        for store in self.stores:
            if store.address == store_address:
                store_found = True
                m = int(input("Какое количество товаров хотите добавить / обновить: "))
                for i in range(m):
                    item_name = input("Введите название товара: ")
                    item_price = float(input("Введите цену товара: "))
                    store.update_item(item_name, item_price)
        if not store_found:
            print("Магазин не найден")

    def remove_item_from_store(self):
        store_address = input("Введите адрес магазина: ")
        store_found = False
        for store in self.stores:
            if store.address == store_address:
                store_found = True
                item_name = input("Введите название товара: ")
                store.remove_item(item_name)
        if not store_found:
            print("Магазин не найден")

    def get_item_range(self):
        store_address = input("Введите адрес магазина: ")
        store_found = False
        for store in self.stores:
            if store.address == store_address:
                store_found = True
                print (store.items)
        if not store_found:
            print("Магазин не найден")


    def get_item_prices(self):
        item_name = input("Введите название товара: ")
        for store in self.stores:
            print(f"Магазин '{store.name}' по адресу: {store.address}")
            print(store.get_item_price(item_name))

    def show_stores(self):
        if len(self.stores) == 0:
            print("магазинов пока нет")
            return
        else:
            i = 1
            for store in self.stores:
                print(f"{i}) '{store.name}' по адресу: {store.address}")
                i += 1

my_stores = Stores()
running = True
while running:
    action = int(input("Выберите действие: "
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
    elif action == 2:
        my_stores.add_item_to_store()
    elif action == 3:
        my_stores.remove_item_from_store()
    elif action == 4:
        my_stores.get_item_prices()
    elif action == 5:
        my_stores.add_item_to_store()
    elif action == 6:
        my_stores.get_item_range()
    elif action == 7:
        my_stores.add_store()
    else:
        running = False