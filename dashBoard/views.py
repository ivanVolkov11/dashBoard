from django.shortcuts import render, get_object_or_404
from dashBoard.models import TaskList
from dashBoard.models import Task
# Create your views here.
class TaskListAndTasck():
    def __init__(self,taskList,tasks):
        self.taskList = taskList
        self.tasks = tasks
def home(request):
    taskLists = TaskList.objects.all()
    TaskListAndTascks = []
    for taskList in taskLists:
        tasks = taskList.entries.all()
        TaskListAndTascks.append(TaskListAndTasck(taskList,tasks))
    context = {
               'taskLists':taskLists,
              'TaskListAndTascks':TaskListAndTascks,
               }
    return render(request,"dashBoard/home.html", context)
def show_task(request, taskID):
    task = get_object_or_404(Task, id = taskID)
    return render(request, "dashBoard/task.html", {'task':task})