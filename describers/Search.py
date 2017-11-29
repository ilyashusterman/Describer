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
            default_value = found_pages[0]
            logging.debug('found_pages={}'.format(found_pages))
            value_found = self.get_found_value(found_pages, default_value)
        else:
            return {'name': 'no_information',
                    'summary': 'no_information'}
        # value_meta = wikipedia.page(value_found)
        try:
            summary = wikipedia.summary(value_found, sentences=sentences)
        except wikipedia.DisambiguationError:
            print (value_found)
            value_meta = wikipedia.page(found_pages[0])
            summary = value_meta.summary(sentences=2)
        return {
            'name': value_found.lower(),
            'summary': str(summary)
        }

    def get_found_value(self, found_values, value_found):
        found_value = value_found
        for keyword_value in found_values:
            if keyword_value == self.keyword.title() or \
                            keyword_value in self.keyword or \
                            self.keyword in keyword_value:
                found_value = keyword_value
                break
        return found_value

    def get_source_analization(self, sentences=2):
        # TODO
        pass
