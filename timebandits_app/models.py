"""Models"""

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone

#Every field with a "0" needs to be replaced with a model format

class Account(models.Model):
    account_name = models.CharField(max_length=40)
    account_id = models.CharField(max_length=40)
    upcoming_tasks = 0 #List of class IDs
    completed_tasks = 0 #List of class IDs
    creation_date = models.DateTimeField('account creation date')
    total_hours = models.IntegerField(default=0)
    user_skills = 0 #List of user skills, need to decide on format
    post_permission = models.BooleanField(default=True)
    volunteer_level = models.IntegerField(default=1)
    def __str__(self):
        return self.account_id

class Task(models.Model):
    owner_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    owner_name = 0 #Do we want to include this here?
    task_id = models.IntegerField(default=0) #Need a function to create unique IDs
    task_title = models.CharField(max_length=100)
    task_description = models.CharField(max_length=500)
    skills_required = 0 #List of skill tags required, need to decide on format
    task_capacity = models.IntegerField(default=1)
    num_volunteers = models.IntegerField(default=0)
    volunteer_ids = 0 #List of volunteer IDs
    time_posted = models.DateTimeField('task creation date')
    event_time = models.DateTimeField('event date') #Optional field
    time_to_complete = models.FloatField(default=1.0) #Should we include a range rather than set amounts?
    event_address = models.CharField(max_length=100) #Seperate into street, city, etc?
    event_latitude = models.FloatField(default=0)
    event_longitude = models.FloatField(default=0)
    task_charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    donation_amount = models.FloatField(default=0.0)
    def addVolunteer(self):
        #function to add volunteer only if there is space
        return 0
    def __str__(self):
        return self.task_title

class Charity(models.Model):
    charity_name = models.CharField(max_length=80)
    charity_description = models.CharField(max_length=400)
    charity_link = models.CharField(max_length=400)
    def __str__(self):
        return self.charity_name