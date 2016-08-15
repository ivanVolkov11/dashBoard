from django.contrib import admin
from dashBoard.models import Task, TaskList

# Register your models here.
admin.site.register([Task,TaskList])
