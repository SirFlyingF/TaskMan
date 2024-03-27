from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Statuses(models.TextChoices):
        TODO = 'TODO', 'To Do'
        PEND = 'PEND', 'In Progress'
        DONE = 'DONE', 'Done'


class Task(models.Model):
    title = models.CharField(max_length=128, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Statuses.choices, default='To Do')

    #table name
    # need to see relevent data for tasks
    
    def get_absolute_url(self):
        # Returns the url for the task-detail url with pk passed
        # Called by CreateView on success. Alternatively can
        # set success_url in classed-ed view to redirect to some other page
        return reverse('task-detail', kwargs={'pk':self.pk})