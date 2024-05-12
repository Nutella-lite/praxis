class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item):
        self.items.update(item)

    def remove_item(self, key):
        self.items.pop(key)

    def get_item(self, key):
        return self.items.get(key, default=None)

    def update_value(self, key):
        self.items.update(key)

class Stores:
    def __init__(self):
        self.stores = []

    def add_store(self, store):
        n = int(input("Какое количество магазинов хотите добавить: "))
        for i in range(n):
            name = input(f"Введите название магазина: ")
            address = input(f"Введите адрес магазина: ")
            store = Store(name, address)
            self.stores.append(store)

    def add_item_to_store(self):
        store_name = input("Введите название магазина: ")
        store = self.get_store_by_name(store_name)
        if store is not None:
            item_name = input("Введите название товара: ")
            item = self.get_item_by_name(item_name)
            if item is not None:
                store.add_item(item)