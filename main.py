from flask import Flask, request, url_for, jsonify, render_template, redirect
import os

from todo import Todo
from roku import Roku

app = Flask(__name__)

todo = Todo(db='todo.db')
tv = Roku(ip=os.environ['roku_ip'])
lights = Hue(ip=os.environ['hue_ip'], username=os.environ['hue_username'])

@app.route('/', methods=['GET', 'POST'])
def index():
    tasks = todo.get()

    if request.method == 'POST' and 'addtask' in request.form:
        task = request.form['addtask']
        todo.post(task)
        tasks = todo.get()
        return render_template("index.html", tasks=tasks)

    if request.method == 'POST' and 'deletetask' in request.form:
        task = request.form['deletetask']
        todo.delete(task)
        tasks = todo.get()
        return render_template("index.html", tasks=tasks)

    if request.method == 'POST' and 'remote' in request.form:
        action = request.form['remote']
        tv.control(action=action)
        return render_template("index.html")

    return render_template("index.html", tasks=tasks)


if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True) 