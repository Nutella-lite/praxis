class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.is_done = False

    def mark_as_done(self):
        self.is_done = True
        print(f"Задача {self.name} помечена как выполненная!")


class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self):
        n = int(input("Какое количество задач хотите добавить: "))
        for i in range(n):
            name = input(f"Введите формулировку задачи: ")
            due_date = input(f"Введите срок выполнения в формате MM.DD: ")
            new_task = Task(name, due_date)
            self.tasks.append(new_task)
    def mark_as_done(self, chosen_name):
        for task in self.tasks:
            if task.name == chosen_name:
                task.mark_as_done()
            else:
                print(f"Задача {chosen_name} не найдена")

    def undone_list(self):
        print("Список текущих задач:")
        active_tasks = [task for task in self.tasks if task.is_done == False]
        if len(active_tasks) == 0:
            print("Нет активных задач")
        else:
            active_tasks.sort(key=lambda task: task.due_date)
            for task in active_tasks:
                print(task.due_date, task.name)


manage = TaskManager()
manage.add_task()
manage.undone_list()
manage.mark_as_done(input("Какую задачу отметить выполненной? "))
manage.undone_list()