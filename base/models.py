from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


Priority_CHOICES = (
    ('High', 'High'),
    ('Normal', 'Normal'),
    ('Low', 'Low'),
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
        ordering = ['updated_on']


class List(AbstractModel):
    title = models.CharField(max_length=200)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.title


class Task(AbstractModel):
    title = models.CharField(max_length=200)
    description = models.TextField(default='', blank=True)
    complete = models.BooleanField(default=False)
    priority = models.CharField(max_length=9, choices=Priority_CHOICES, default='Normal')
    list_no = models.ForeignKey(List, on_delete=models.CASCADE, null=True, blank=True)
    due_date = models.DateTimeField(default=one_week_hence)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete',"due_date"]
