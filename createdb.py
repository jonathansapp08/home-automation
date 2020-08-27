import shelve

todo = shelve.open('todo.db')
try:
    todo['1'] = { 'Wash the dishes' }
finally:
    todo.close()