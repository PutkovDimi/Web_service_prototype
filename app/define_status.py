from app import db, models
from datetime import datetime
from .calculate_time import get_time_of_end

'''
Соответственно определяем:
Если на данный момент время старта задачи не подошло - > In queue
Если данный момент времени меньше,чем время окончания -> Run
Иначе Completed
'''


def define_status(id):
    cur_time = datetime.now().time()
    start_time = datetime.strptime(models.Task.query.get(id).start_time, "%H:%M:%S.%f").time()
    if cur_time < start_time:
        return 'In Queue'
    elif cur_time < get_time_of_end(id):
        return 'Run'
    else:
        return 'Completed'
