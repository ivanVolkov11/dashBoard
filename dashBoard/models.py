from django.db import models

# Create your models here.
class TaskList(models.Model):
    title = models.CharField(max_length = 200)
    def __str__(self):
        return self.title
class Task(models.Model):
    title = models.CharField(max_length = 200)
    description= models.TextField()
    startDate = models.DateField(auto_now_add=True)
    endDate = models.DateField(blank = True)
    status = models.CharField(choices=(("is done","done"),
                                       ("in work","in work")),
                                       default = "in work",
                                       max_length = 10)
    taskList = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='entries')
    def __str__(self):
        return self.title
    