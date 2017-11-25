from unittest import TestCase


class TestRecognition(TestCase):
    def setUp(self):
        with open('test_image.png') as data_file:
            self.test_image = data_file
