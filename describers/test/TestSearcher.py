from unittest import TestCase

from describers.Searcher import Searcher


class TestDescriptor(TestCase):
    def setUp(self):
        self.keyword = 'dog'

    def test_keyword_search(self):
        keyword = 'dog'
        s = Searcher(keyword)
        analization = s.get_analyzization()
        self.assertEqual(analization['name'], 'dog')