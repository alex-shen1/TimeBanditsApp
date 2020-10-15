"""Tests for the site"""
from django.test import TestCase


class TrivialTest(TestCase):
    """Contains trivial tests"""

    def test_trivial_math(self):
        """Most trivial possible test to verify testing works."""
        self.assertTrue(1 + 1 == 2)
