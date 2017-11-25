from unittest import TestCase


class TestDescription(TestCase):
    def setUp(self):
        with open('test_mouse.jpg') as data_file:
            self.test_image = data_file
