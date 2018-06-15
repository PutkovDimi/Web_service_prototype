import random
from app import db, models
from datetime import datetime, timedelta
import time
import random

'''
Идея в следующем:
Если задачи в очереди под номерами 1 или 2, то эти задачи будут выполняться первыми и 
их время старта не зависит от других задач. Также учитвается, что время создания задачи меньше(или больше)
времени, за которое первые две задачи выполняться
Для всех остальных мы рассчитываем ближайшее время из двух задач, стояших перед ними
Так как этот расчет запускается каждый раз при добавлении нового элемента в таблицу,
гарантированно, что у каждого будет точное и минимальное время старта
'''


def get_shortest_time(id, create_time):
    create_time = datetime.strptime(create_time, "%H:%M:%S.%f").time()
    print('create time ', create_time)
    time_of_last_1 = get_time_of_end(id - 1)
    time_of_last_2 = get_time_of_end(id - 2)
    min_time = min(time_of_last_1, time_of_last_2)
    print(min_time)
    if create_time > min_time:
        return create_time
    return min_time


def calculate_time(id, create_time):
    if id == 1 or id == 2:
        return create_time
    else:
        return str(get_shortest_time(id, create_time))


def get_time_of_end(id):
    start_time = datetime.strptime(models.Task.query.get(id).start_time, "%H:%M:%S.%f")
    time_of_end = start_time + timedelta(seconds=int(models.Task.query.get(id).execution_time))
    return time_of_end.time()


def exec_time():
    return random.randint(0, 10)


'''if __name__ == "__main__":
    tasks = models.Task.query.all()
    for t in tasks:
        db.session.delete(t)
    db.session.commit()'''
