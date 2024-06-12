import unittest
from todo import ToDoList


class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo_list = ToDoList()

    def test_add_task(self):
        self.todo_list.add_task("Task 1")
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0], "Task 1")

    def test_remove_task(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.delete_task(1)
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0], "Task 1")

    def test_show_tasks(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        tasks = self.todo_list.list_tasks()
        self.assertEqual(tasks, ["Task 1", "Task 2"])


if __name__ == "__main__":
    unittest.main()
