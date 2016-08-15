from django.conf.urls import url
from dashBoard.views import home, show_task

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^tasks/(?P<taskID>[0-9]+)$', show_task, name='task'),
]