"""Tests for the site"""
from django.test import TestCase
from timebandits_app.models import Task
from timebandits_app.forms.task_form import TaskForm

class TrivialTest(TestCase):
    """Contains trivial tests"""

    def test_trivial_math(self):
        """Most trivial possible test to verify testing works."""
        self.assertTrue(1 + 1 == 2)

class TaskTest(TestCase):
    """Tests TaskForm Validators"""
    
    def test_invalid_capacity(self):
        """Tests that tasks with negative capacity fails."""
        form_data={"task_title":"Testing!","task_description":"Test Description","task_capacity":"1","num_volunteers":"0","event_date":"2020-12-12","time_to_complete":"1","donation_amount":"0","event_address":"Down the road"}
        form_data["task_capacity"] = "-1"
        form = TaskForm(form_data)
        self.assertEquals(form.errors['task_capacity'], [u"Task capacity cannot be negative."])
        self.assertFalse(form.is_valid())

    def test_valid_capacity(self):
        """Tests that tasks with positive capacity pass."""
        form_data={"task_title":"Testing!","task_description":"Test Description","task_capacity":"1","num_volunteers":"0","event_date":"2020-12-12","time_to_complete":"1","donation_amount":"0","event_address":"Down the road"}
        form_data["task_capacity"] = "1"
        form = TaskForm(form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_date(self):
        """Tests that tasks with date in the past fail."""
        form_data={"task_title":"Testing!","task_description":"Test Description","task_capacity":"1","num_volunteers":"0","event_date":"2020-12-12","time_to_complete":"1","donation_amount":"0","event_address":"Down the road"}
        form_data["event_date"] = "2020-08-08"
        form = TaskForm(form_data)
        self.assertEquals(form.errors['event_date'], [u"Event cannot be in the past!"])

    def test_valid_date(self):
        """Tests that tasks with valid dates pass."""
        form_data={"task_title":"Testing!","task_description":"Test Description","task_capacity":"1","num_volunteers":"0","event_date":"2020-12-12","time_to_complete":"1","donation_amount":"0","event_address":"Down the road"}
        form_data["event_date"] = "2021-09-09"
        form = TaskForm(form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_timetocomplete(self):
        """Tests that tasks with negative time_to_complete fail."""
        form_data={"task_title":"Testing!","task_description":"Test Description","task_capacity":"1","num_volunteers":"0","event_date":"2020-12-12","time_to_complete":"1","donation_amount":"0","event_address":"Down the road"}
        form_data["time_to_complete"] = "-1"
        form = TaskForm(form_data)
        self.assertEquals(form.errors['time_to_complete'], [u"Time to complete must be a positive number."])

    def test_valid_timetocomplete(self):
        """Tests that tasks with valid time_to_complete pass."""
        form_data={"task_title":"Testing!","task_description":"Test Description","task_capacity":"1","num_volunteers":"0","event_date":"2020-12-12","time_to_complete":"1","donation_amount":"0","event_address":"Down the road"}
        form_data["time_to_complete"] = "1"
        form = TaskForm(form_data)
        self.assertTrue(form.is_valid())

    def test_toohigh_donation(self):
        """Tests that tasks with donations over $200 maximum fail."""
        form_data={"task_title":"Testing!","task_description":"Test Description","task_capacity":"1","num_volunteers":"0","event_date":"2020-12-12","time_to_complete":"1","donation_amount":"0","event_address":"Down the road"}
        form_data["donation_amount"] = "1001"
        form = TaskForm(form_data)
        self.assertEquals(form.errors['donation_amount'], [u"1001.0 is not within donation range of 0 - 200"])

    def test_toolow_donation(self):
        """Tests that tasks with donations over $200 maximum fail."""
        form_data={"task_title":"Testing!","task_description":"Test Description","task_capacity":"1","num_volunteers":"0","event_date":"2020-12-12","time_to_complete":"1","donation_amount":"0","event_address":"Down the road"}
        form_data["donation_amount"] = "-5"
        form = TaskForm(form_data)
        self.assertEquals(form.errors['donation_amount'], [u"-5.0 is not within donation range of 0 - 200"])

    def test_valid_donation(self):
        """Tests that tasks with valid time_to_complete pass."""
        form_data={"task_title":"Testing!","task_description":"Test Description","task_capacity":"1","num_volunteers":"0","event_date":"2020-12-12","time_to_complete":"1","donation_amount":"0","event_address":"Down the road"}
        form_data["donation_amount"] = "100"
        form = TaskForm(form_data)
        self.assertTrue(form.is_valid())
