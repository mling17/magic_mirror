from stark.service.v1 import site, StarkHandler
from mirror import models


class ToDoHandler(StarkHandler):
    list_display = ['title','date','period','fix_day']


site.register(models.ToDo,ToDoHandler)
