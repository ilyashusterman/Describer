from unittest import TestCase

from describers.Recognition import Recognition
from describers.Search import Search


class TestDescription(TestCase):

    def test_description_of_desk_image(self):
        item = 'desk'
        recognition = Recognition('test/test_{}.jpg'.format(item))
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