from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TAGS_CHOICES = (
    ('green', 'GREEN'),
    ('yellow', 'YELLOW'),
    ('orange', 'ORANGE'),
    ('red', 'RED'),
    ('black', 'BLACK'),
)
LISTS_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)


class AbstractModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_requests_created')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_requests_updated')
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_requests_deleted')

        
    class Meta:
        abstract = True

class Task(AbstractModel):
    
    title = models.CharField(max_length=200)
    description = models.TextField(default='', blank=True)
    complete = models.BooleanField(default=False)
    tags = models.CharField(max_length=6, choices=TAGS_CHOICES, default='GREEN')


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


class List(AbstractModel):
    
    title = models.CharField(max_length=200)
    description = models.TextField(default='', blank=True)
    

    def __str__(self):
        return self.title

