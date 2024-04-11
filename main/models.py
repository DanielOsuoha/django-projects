from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todo(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo', null=True)
    
    
    def __str__(self):
        return self.title
class item(models.Model):
    text = models.TextField(max_length=400)
    complete = models.BooleanField()
    todolist = models.ForeignKey(todo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text
