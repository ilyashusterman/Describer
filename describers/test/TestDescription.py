from unittest import TestCase
from unipath import Path

from describers.Recognition import Recognition
from describers.Search import Search


class TestDescription(TestCase):

    def test_description_of_desk_image(self):
        item = 'desk'
        recognition = Recognition(Path(Path(__file__).parent, 'test_{}.jpg'.format(item)))
        classification = recognition.classify_image()
        self.assertTrue('{}'.format(item) in classification['value'],
                        classification)
        summary = 'A desk or bureau is a piece of furniture with a flat ' \
                  'table-style work surface used in a school, office, ' \
                  'home or the like for academic, professional or domestic' \
                  ' activities such as reading, writing, or using equipment ' \
                  'such as a computer.  Desks often have one or ' \
                  'more drawers, ' \
                  'compartments, or pigeonholes to store items' \
                  ' such as office supplies and papers.'
        search = Search(classification['value'])
        analization = search.get_analyzization(sentences=2)
        self.assertEqual(len(analization['summary']), len(summary),
                         analization)

    def test_description_of_door_image(self):
        item = 'door'
        recognition = Recognition(Path(Path(__file__).parent,
                                       'test_{}.jpg'.format(item)))
        classification = recognition.classify_image()
        self.assertTrue('{}'.format(item) in classification['value'],
                        classification)
        summary = 'A door is a moving mechanism used to block off,' \
                  ' and allow access to, an entrance to or within ' \
                  'an enclosed space, such as a building,' \
                  ' room or vehicle. Doors normally consist ' \
                  'of one or two solid panels, with or without' \
                  ' windows, that swing on hinges horizontally.'
        search = Search(classification['value'])
        analization = search.get_analyzization(sentences=2)
        self.assertEqual(len(analization['summary']), len(summary),
                         analization)

    def test_description_of__image(self):
        item = 'bottle'
        recognition = Recognition(Path(Path(__file__).parent,
                                       'test_{}.jpg'.format(item)))
        classification = recognition.classify_image()
        self.assertTrue('{}'.format(item) in classification['value'],
                        classification)
        summary = 'A bottle is a rigid container with a neck' \
                  ' that is narrower than the body and a mouth. ' \
                  'By contrast, a jar has a relatively large ' \
                  'mouth or opening which may be as wide as' \
                  ' the overall container.'
        search = Search(classification['value'])
        analization = search.get_analyzization(sentences=2)
        self.assertEqual(len(analization['summary']), len(summary),
                         analization)
