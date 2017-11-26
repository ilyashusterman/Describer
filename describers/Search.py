import logging
import wikipedia


class Search(object):
    def __init__(self, keyword):
        if ' ' in keyword:
            keyword = keyword.replace(' ', '')
        self.keyword = keyword

    def get_analyzization(self, sentences=2):
        found_pages = wikipedia.search(self.keyword)
        if len(found_pages) > 0:
            value_found = found_pages[0]
            # citi_value_found = citi_found_pages[0]
            logging.debug('found_pages={}'.format(found_pages))
            # ‎TODO need to refactor assertion
            assert value_found == self.keyword.title() or \
                   value_found in self.keyword or \
                   self.keyword in value_found
        else:
            return {'name': 'no_information'}
        # value_meta = wikipedia.page(value_found)
        summary = wikipedia.summary(value_found, sentences=sentences)
        return {
            'name': value_found.lower(),
            'summary': str(summary)
        }

    def get_source_analization(self, sentences=2):
        #TODO
        pass