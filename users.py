class User:
  def __init__(self, id, name):
    self.__id = id
    self.__name = name
    self._level = 'user'

  def get_user(self):
    return f" {self.__name}, id = {self.__id}, уровень доступа = {self._level}"


class Admin(User):
  def __init__(self, id, name):
    super().__init__(id, name)
    self._level = 'admin'
    self.users = []

  def add_user(self):
    NAME = input("Введите имя нового пользователя: ")
    ID = len(self.users) + 1
    lev = int(input("Введите уровень доступа нового пользователя: 1 = user, 2 = admin \n"))
    if lev == 1:
      USER = User(ID, NAME)
    else:
      USER = Admin(ID, NAME)
    print(f"Добавлен пользователь {USER.get_user()}")
    self.users.append(USER)

  def remove_user(self):
    NAME = input("Введите имя пользователя, которого нужно исключить: ")
    USER = next((user for user in self.users if user._User__name == NAME), None)  # mangling
    if USER is not None:
      print(f"Удален пользователь {USER.get_user()}")
      self.users.remove(USER)
    else:
      print(f"Пользователь с именем {NAME} не найден")

  def get_all_users(self):
    for user in self.users:
      print(user.get_user())


my_users = Admin(0, "admin") # Первого админа в список не добавляем
running = True
while running:
  action = int(input("Выберите действие: "
                     "\n1 - показать список пользователей "
                     "\n2 - добавить пользователя "
                     "\n3 - удалить пользователя "
                     "\n4 - выход из программы \n"))
  if action == 1:
    my_users.get_all_users()
  elif action == 2:
    my_users.add_user()
  elif action == 3:
    my_users.remove_user()
  else:
    running = False
