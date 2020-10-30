"""Models"""

# Create your models here.
import datetime
from django.db import models
# from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms

# from django.contrib.postgres.fields import ArrayField
# from django.utils import timezone

# Validators

def validate_task_capacity(value):
    """Verifies that task_capacity and num_volunteers is positive"""
    if value < 0:
        raise ValidationError(
            _('Task capacity cannot be negative.'),
            params={'value': value},
        )


def validate_time_to_complete(value):
    """Verifies that time_to_complete is positive"""
    if value <= 0:
        raise ValidationError(
            _('Time to complete must be a positive number.'),
            params={'value': value},
        )


def validate_event_date(value):
    """Verifies that event_date is in the future"""
    if value.date() < datetime.date.today():
        raise ValidationError(
            _('Event cannot be in the past!'),
            params={'value': value},
        )


def validate_donation_amount(value):
    """# Verifies that donation is between 0 - 200"""
    if value < 0 or value > 200:
        raise ValidationError(
            _('%(value)s is not within donation range of 0 - 200'),
            params={'value': value},
        )


# Every field with a "0" needs to be replaced with a model format


class Account(models.Model):
    """Account data model. Can have many Tasks."""
    account_name = models.CharField(max_length=40)
    account_id = models.CharField(max_length=40)
    upcoming_tasks = 0  # List of class IDs
    completed_tasks = 0  # List of class IDs
    creation_date = models.DateTimeField('account creation date')
    total_hours = models.IntegerField(default=0)
    user_skills = 0  # List of user skills, need to decide on format
    post_permission = models.BooleanField(default=True)
    volunteer_level = models.IntegerField(default=1)

    def __str__(self):
        return self.account_id


class Charity(models.Model):
    """Charity model"""
    charity_name = models.CharField(max_length=80)
    charity_description = models.CharField(max_length=400)
    charity_link = models.CharField(max_length=400)

    def __str__(self):
        return self.charity_name


class Task(models.Model):
    """Task model. Owned by an Account, linked to a Charity."""

    # I've commented out some of the fields that require other infrastructure
    # to make CRUD easier. We can integrate those in the future.

    # owner_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    # owner_name = 0  # Do we want to include this here?
    # task_id = models.IntegerField(default=0)  # Need a function to create unique IDs
    # task_id = models.AutoField(primary_key=True) # gives an error
    task_title = models.CharField(max_length=100)
    task_description = models.CharField(max_length=500)
    # skills_required = 0  # List of skill tags required, need to decide on format
    # skills_required = ArrayField(models.CharField(max_length=50, blank=True))
    task_capacity = models.IntegerField(
        default=1, validators=[validate_task_capacity])
    num_volunteers = models.IntegerField(
        default=0, validators=[validate_task_capacity])
    # volunteer_ids = 0  # List of volunteer IDs
    time_posted = models.DateTimeField('task creation date', auto_now=True)
    event_date = models.DateTimeField(
        'event date', validators=[validate_event_date])  # Optional field
    time_to_complete = models.FloatField(
        default=1.0, validators=[validate_time_to_complete])
    # Should we include a range rather than set amounts?
    # Separate into street, city, etc?
    event_address = models.CharField(max_length=100)
    # event_latitude = models.FloatField(default=0)
    # event_longitude = models.FloatField(default=0)
    # task_charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    donation_amount = models.FloatField(
        default=0.0, validators=[validate_donation_amount])

    # commented out so pylint doesn't get mad
    # def add_volunteer(self):
    #     """Adds volunteer only if there is space"""
    #     # function to add volunteer only if there is space
    #     return 0

    def __str__(self):
        return self.task_title
