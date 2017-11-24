from unittest import TestCase

from describers.Searcher import Searcher


class TestDescriptor(TestCase):
    def setUp(self):
        self.keyword = 'dog'

    def test_keyword_search(self):
        keyword = 'dog'
        summary = 'The domestic dog (Canis lupus familiaris or Canis ' \
                  'familiaris) is a wolf-like canid￼￼ in the genus Canis, ' \
                  'and is the most numerous and widely distributed member ' \
                  'of the order Carnivora. The dog and the extant gray wolf￼' \
                  ' are sister taxa as modern wolves are not closely related ' \
                  'to the wolves that were first domesticated, which ' \
                  'implies that the direct ancestor of the dog is extinct.'
        s = Searcher(keyword)
        analization = s.get_analyzization()
        self.assertEqual(analization.get('name'), 'dog')
        self.assertEqual(analization.get('summary'), summary)