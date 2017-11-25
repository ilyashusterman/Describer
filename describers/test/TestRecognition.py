from unittest import TestCase

from describers.Recognition import Recognition


class TestRecognition(TestCase):
    def setUp(self):
        with open('test_image.png') as data_file:
            self.test_image = data_file

    def test_mouse_image_classification(self):
        recognition = Recognition('test_mouse.jpg')
        classification = recognition.classify_image()
        self.assertTrue('computer mouse' in classification['value'])