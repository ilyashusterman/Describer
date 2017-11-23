from unittest import TestCase

from describers.Searcher import Searcher


class TestDescriptor(TestCase):
    def setUp(self):
        with open('test_image.png') as data_file:
            self.test_image = data_file

    def test_keyword_search(self):
        keyword = 'dog'
        s = Searcher(keyword)
        analization = s.get_analyzization()
        self.assertEqual(analization['name'], 'dog')