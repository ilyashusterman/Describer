from unittest import TestCase

from describers.Search import Search


class TestDescriptor(TestCase):
    def setUp(self):
        self.keyword = 'dog'

    def test_keyword_search(self):
        keyword = 'dog'
        summary = 'The domestic dog (Canis lupus familiaris or' \
                  ' Canis familiaris) is a wolf-like canid and a' \
                  ' member of the genus Canis, and is the most abundant ' \
                  'carnivore. The dog and the extant gray wolf are sister ' \
                  'taxa as modern wolves are not closely related to ' \
                  'the wolves that were first domesticated, ' \
                  'which implies that the direct ancestor of ' \
                  'the dog is extinct.'
        s = Search(keyword)
        analization = s.get_analyzization()
        self.assertEqual(analization.get('name'), 'dog')
        self.assertEqual(len(analization.get('summary')), len(summary),
                         analization)

    def test_analization_summary_of_3_sentences(self):
        summary = 'A smartphone is a handheld personal computer with a ' \
                  'mobile operating system and an integrated mobile' \
                  ' broadband cellular network connection for voice, ' \
                  'SMS, and Internet data communication; most if not' \
                  ' all smartphones also support Wi-Fi. Smartphones ' \
                  'are typically pocket-sized, as opposed to tablets, ' \
                  'which are much larger than a pocket. ' \
                  'They are able to run a variety of ' \
                  'third-party software components ("apps") ' \
                  'from places like the Google Play Store or Apple App ' \
                  'Store, and can receive bug fixes and gain additional ' \
                  'functionality through operating system software updates.'

        search = Search('smartphone')
        analization = search.get_analyzization(sentences=3)
        self.assertEqual(len(analization['summary']), len(summary),
                         analization)