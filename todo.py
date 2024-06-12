class ToDoList:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def mark_task_done(self, task):
        if task in self.tasks:
            index = self.tasks.index(task)
            self.tasks[index] = f"{task} (done)"
            self.save_tasks()

    def list_tasks(self):
        return self.tasks.copy()
