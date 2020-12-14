"""Tests for the site"""
# pylint: disable=imported-auth-user

from django.test import TestCase
from django.contrib.auth.models import User

from timebandits_app.forms.task_form import TaskForm

from ..templatetags import formatters


class TrivialTest(TestCase):
    """Contains trivial tests"""

    def test_trivial_math(self):
        """Most trivial possible test to verify testing works."""
        self.assertTrue(1 + 1 == 2)


class CurrencyFormatterTest(TestCase):
    """Contains test cases for the formatter"""

    def test_short_decimal(self):
        """Test one decimal place"""
        self.assertTrue(formatters.currency(200.0), "$200.00")

    def test_no_decimal(self):
        """Test no decimal points"""
        self.assertTrue(formatters.currency(20), "$20.00")

    def test_long_decimal(self):
        """Test 3 decimal places"""
        self.assertTrue(formatters.currency(2.0000), "$2.00")

    def test_zero(self):
        """Test 0"""
        self.assertTrue(formatters.currency(0), "$0.00")


class VolunteerLevelFormatter(TestCase):
    """Contains test cases for the formatter"""

    def test_vl_formatter1(self):
        """Test when volunteer level is 12"""
        self.assertTrue(formatters.volunteer_level(12), "2")

    def test_vl_formatter2(self):
        """Test when volunteer level is -1"""
        self.assertTrue(formatters.volunteer_level(-1), "0")

    def test_vl_formatter3(self):
        """Test when volunteer level is 0"""
        self.assertTrue(formatters.volunteer_level(0), "1")


class TaskTest(TestCase):
    """Tests TaskForm Validators"""

    form_data_template = {
        "task_title": "Testing!",
        "task_description": "Test Description",
        "task_capacity": "1",
        "event_date": "2020-12-12",
        "time_to_complete": "1",
        "donation_amount": "0",
        "event_address": "Down the road"}

    def test_invalid_capacity(self):
        """Tests that tasks with negative capacity fails."""
        user = User.objects.create_user(
            username='testuser', password='12345')
        form_data = self.form_data_template.copy()
        form_data["task_capacity"] = "-1"
        form_data["owner"] = user.account
        form = TaskForm(form_data)
        self.assertEqual(
            form.errors['task_capacity'],
            [u"Task capacity cannot be negative."])
        self.assertFalse(form.is_valid())

    def test_invalid_date(self):
        """Tests that tasks with date in the past fail."""
        user = User.objects.create_user(
            username='testuser', password='12345')
        form_data = self.form_data_template.copy()
        form_data["event_date"] = "2020-08-08"
        form_data["owner"] = user.account
        form = TaskForm(form_data)
        self.assertEqual(
            form.errors['event_date'],
            [u"Event cannot be in the past!"])

    def test_valid_date(self):
        """Tests that tasks with valid dates pass."""
        user = User.objects.create_user(
            username='testuser', password='12345')
        form_data = self.form_data_template.copy()
        form_data["event_date"] = "2021-09-09"
        form_data["owner"] = user.account
        form = TaskForm(form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_time_to_complete(self):
        """Tests that tasks with negative time_to_complete fail."""
        user = User.objects.create_user(
            username='testuser', password='12345')
        form_data = self.form_data_template.copy()
        form_data["time_to_complete"] = "-1"
        form_data["owner"] = user.account
        form = TaskForm(form_data)
        self.assertEqual(
            form.errors['time_to_complete'],
            [u"Time to complete must be a positive number."])

    def test_too_high_donation(self):
        """Tests that tasks with donations over $200 maximum fail."""
        user = User.objects.create_user(
            username='testuser', password='12345')
        form_data = self.form_data_template.copy()
        form_data["donation_amount"] = "1001"
        form_data["owner"] = user.account
        form = TaskForm(form_data)
        self.assertEqual(
            form.errors['donation_amount'],
            [u"1001.0 is not within donation range of 0 - 200"])

    def test_too_low_donation(self):
        """Tests that tasks with donations over $200 maximum fail."""
        user = User.objects.create_user(
            username='testuser', password='12345')
        form_data = self.form_data_template.copy()
        form_data["donation_amount"] = "-5"
        form_data["owner"] = user.account
        form = TaskForm(form_data)
        self.assertEqual(
            form.errors['donation_amount'],
            [u"-5.0 is not within donation range of 0 - 200"])
