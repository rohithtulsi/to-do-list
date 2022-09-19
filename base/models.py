from pyexpat import model
from statistics import mode
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TAGS_CHOICES = (
    ('green','GREEN'),
    ('yellow', 'YELLOW'),
    ('orange','ORANGE'),
    ('red','RED'),
    ('black','BLACK'),
)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) 
    tags = models.CharField(max_length=6, choices=TAGS_CHOICES, default='GREEN')

    def __str__(self):
        return self.title


    class Meta:
        ordering=['complete']