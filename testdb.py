import shelve

todo = shelve.open('todo.db')
try:
    print(todo['1'])
finally:
    todo.close()