from flask import jsonify
import shelve

class Todo():
    def __init__(self, db):
        self.db = db

    def get(self):
        """
        View all tasks in the the todo list.
        """
        todo = shelve.open('todo.db')
        tasks = todo.keys()

        todolist = {}
        for task in tasks:
            todolist[task] = todo[task]
        return todolist.items()

    def post(self, task):
        """
        Add a new task to the todo list.
        """
        try:
            todo = shelve.open(self.db)
            todo[str(len(todo) + 1)] = [task]
            todo.close()
            return '201'
        except:
            return 'Error'

    def delete(self, task):
        """
        Delete a task from the todo list.
        """
        try:
            todo = shelve.open(self.db)
            del todo[task]
            print('deleted')
            return('204')
        except:
            return('Error')
        finally:
            todo.close()