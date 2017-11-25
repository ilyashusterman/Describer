from unittest import TestCase

from describers.Recognition import Recognition


class TestRecognition(TestCase):
    def setUp(self):
        pass

    def test_mouse_image_classification(self):
        recognition = Recognition('test/test_mouse.jpg')
        classification = recognition.classify_image()
        self.assertTrue('computer mouse' in classification['value'])