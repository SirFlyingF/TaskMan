from django.urls import path
from .views import TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView, TaskCreateView

urlpatterns = [
    path('home/', TaskListView.as_view(), name='task-home'),
    path('<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),
    path('create/', TaskCreateView.as_view(), name='task-create')
]



#301 -> response code
'''response codes required for us
    3xx -4Xx 5XX - imp
    2XX - good to know'''