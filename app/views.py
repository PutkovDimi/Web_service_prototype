from app import app
from flask import render_template, request
from app import models, db
from datetime import datetime
from .calculate_time import calculate_time, exec_time
from .get_last_task import get_last_task
from .proccess_to_JSON import proccess_to_JSON


@app.route('/', methods=["GET", "POST"])
def create_task():
    max_numb = get_last_task()
    print(max_numb)
    if request.method == "POST":
        create_time = str(datetime.now().time())
        start_time = calculate_time(max_numb + 1, create_time)
        execution_time = exec_time()
        task = models.Task(create_time=create_time, start_time=start_time, execution_time=execution_time)
        db.session.add(task)
        db.session.commit()
        max_numb += 1
    return render_template("add_task.html", number=max_numb)


@app.route('/get_status/', methods=["GET", "POST"])
@app.route('/get_status<number>', methods=["GET", "POST"])
def get_status(number=None):
    if not number:
        number = get_last_task()  # Если не передали номер задачи- по умолчанию берем последнюю
    task_info = proccess_to_JSON(number)
    return render_template("get_status.html", task=task_info)
