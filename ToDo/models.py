from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime

# Create your models here.

class Todo(models.Model):
    title = models.CharField( max_length=50, blank=False,null=False)
    start_date = models.DateField(default = datetime.date.today)
    start_time = models.TimeField(default= datetime.datetime.now)

    class Meta:
        get_latest_by ='start_time'


    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})


