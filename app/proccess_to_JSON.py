from .define_status import define_status
from app import db, models


def proccess_to_JSON(id):
    dict_info = {'status': '', 'create_time': '', 'start_time': '', 'time_to_execute': ''}
    dict_info.update({'status': define_status(id),
                      'create_time': models.Task.query.get(id).create_time,
                      'start_time': models.Task.query.get(id).start_time,
                      'time_to_execute': models.Task.query.get(id).execution_time})
    return dict_info
