from django.test import TestCase


class TrivialTest(TestCase):
    def testOnePlusOneEqualsTwo(self):
        self.assertTrue(1 + 1 == 2)
