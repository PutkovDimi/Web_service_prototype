# Web_service_prototype
There is a web service prototype.

###How to run:

1. `./setup_dependencies.sh`

2. `python3 db_create.py`

3. `python3 run.py`

Now you've run local server with app. By default address  you may create task. By address */get_statusN*, where N = number of task you may get json-formatted string with info about the task. N = number of last task. 

It realizes the idea that when you create task, it's automatically added into queue, and it waits for its queue. It works as an organizer - it calculates when it starts to complete and when it finishes.

There are some notices into `define_status.py` and `calculate_time.py`

