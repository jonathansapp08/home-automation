from flask import Flask, request, url_for, jsonify, render_template, redirect
import os

from todo import Todo
from roku import Roku
from hue import Hue

app = Flask(__name__)

todo = Todo(db='todo.db')
tv = Roku(ip=os.environ['roku_ip'])
light = Hue(ip=os.environ['hue_ip'], username=os.environ['hue_username'])

@app.route('/', methods=['GET', 'POST'])
def index():
    tasks = todo.get()
    lights = light.get()

    if request.method == 'POST' and 'addtask' in request.form:
        task = request.form['addtask']
        todo.post(task)
        tasks = todo.get()
        return render_template("index.html", tasks=tasks, lights=lights)

    if request.method == 'POST' and 'deletetask' in request.form:
        task = request.form['deletetask']
        todo.delete(task)
        tasks = todo.get()
        return render_template("index.html", tasks=tasks, lights=lights)

    if request.method == 'POST' and 'remote' in request.form:
        action = request.form['remote']
        tv.control(action=action)
        return render_template("index.html", tasks=tasks, lights=lights)   

    if request.method == 'POST' and 'toggle' in request.form:
        light_id = request.form['toggle']
        current_state = lights[light_id]['state']['on']
        light.toggle(light_id=light_id, current_state=current_state)
        lights = light.get()
        return render_template("index.html", tasks=tasks, lights=lights)

    return render_template("index.html", tasks=tasks, lights=lights)


if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port=5001, debug = True) 