from unittest import TestCase
from unipath import Path

from describers.Recognition import Recognition


class TestRecognition(TestCase):
    def test_mouse_image_classification(self):
        recognition = Recognition(Path(Path(__file__).parent, 'test_mouse.jpg'))
        classification = recognition.classify_image()
        self.assertTrue('computer mouse' in classification['value'],
                        classification)

    def test_desk_image_classification(self):
        recognition = Recognition(Path(Path(__file__).parent, 'test_desk.jpg'))
        classification = recognition.classify_image()
        self.assertTrue('desk' in classification['value'],
                        classification)
