from unittest import TestCase
from unipath import Path

from describers.Recognition import Recognition
from describers.Search import Search


class TestDescription(TestCase):
    def test_description_of_desk_image(self):
        item = 'desk'
        summary = 'A desk or bureau is a piece of furniture with a flat ' \
                  'table-style work surface used in a school, office, ' \
                  'home or the like for academic, professional or domestic' \
                  ' activities such as reading, writing, or using equipment ' \
                  'such as a computer.  Desks often have one or ' \
                  'more drawers, ' \
                  'compartments, or pigeonholes to store items' \
                  ' such as office supplies and papers.'
        self.check_image(item, summary)

    def test_description_of_door_image(self):
        item = 'door'
        summary = 'A door is a moving mechanism used to block off,' \
                  ' and allow access to, an entrance to or within ' \
                  'an enclosed space, such as a building,' \
                  ' room or vehicle. Doors normally consist ' \
                  'of one or two solid panels, with or without' \
                  ' windows, that swing on hinges horizontally.'
        self.check_image(item, summary)

    def test_description_of_plate_image(self):
        item = 'plate'
        summary = 'no_information'
        self.check_image(item, summary)

    def test_description_of_bottle_image(self):
        item = 'bottle'
        summary = 'A bottle is a rigid container with a neck' \
                  ' that is narrower than the body and a mouth. ' \
                  'By contrast, a jar has a relatively large ' \
                  'mouth or opening which may be as wide as' \
                  ' the overall container.'
        self.check_image(item, summary)

    def test_description_of_sheep_image(self):
        item = 'wolf'
        summary = 'The gray wolf or grey wolf (Canis lupus), also known ' \
                  'as the timber wolf or western wolf, is a canine ' \
                  'native to the wilderness and remote areas of Eurasia ' \
                  'and North America. It is the largest extant member of ' \
                  'its family, with males averaging 43–45 kg (95–99 lb)' \
                  ' and females 36–38.5 kg (79–85 lb).'
        self.check_image(item, summary)

    def check_image(self, item, summary):
        recognition = Recognition(Path(Path(__file__).parent,
                                       'test_{}.jpg'.format(item)))
        classification = recognition.classify_image()
        self.assertTrue('{}'.format(item) in classification['value'],
                        classification)
        search = Search(classification['value'])
        analization = search.get_analyzization(sentences=2)
        self.assertEqual(len(analization['summary']), len(summary),
                         'analization={} summary={}'
                         .format(analization, summary))
