import logging
import wikipedia


class Search(object):
    SEARCH_COUNT = 1
    SUMMARY_DEFAULT_MESSAGE = 'no_further_information'
    def __init__(self, keyword):
        if keyword.strip().find(' ') != -1:
            keyword = keyword.split(' ')[0]
        if ' ' in keyword:
            keyword = keyword.replace(' ', '')
        self.keyword = keyword.title()

    def get_analyzization(self, sentences=2):
        logging.debug('self.keyword={}'.format(self.keyword))
        found_pages = wikipedia.search(self.keyword)
        logging.debug('found_pages={}'.format(found_pages))
        if len(found_pages) > 0:
            default_value = found_pages[0]
            logging.debug('found_pages={}'.format(found_pages))
            # value_found = self.get_found_value(found_pages, default_value)
            value_found = default_value
        else:
            return {'name': self.keyword,
                    'summary': self.SUMMARY_DEFAULT_MESSAGE}
        # value_meta = wikipedia.page(value_found)
        summary, value_found = self.get_summary(found_pages,
                                                sentences,
                                                value_found)
        return {
            'name': value_found.lower(),
            'summary': str(summary)
        }

    def get_summary(self, found_pages, sentences, value_found):
        try:
            summary = wikipedia.summary(value_found,
                                        sentences=sentences)
        except wikipedia.DisambiguationError:
            summary, value_found = self.handle_summary(found_pages, sentences)
            pass
        return summary, value_found

    def handle_summary(self, found_pages, sentences):
        time_counts = 0
        value_found = found_pages[0]
        summary = None
        while time_counts < self.SEARCH_COUNT:
            try:
                summary = wikipedia.summary(value_found, sentences=sentences)
            except wikipedia.DisambiguationError as e:
                summary = None
                # TODO need to fix this options summary from other source
                # options = [option for option in e.options
                #            if self.keyword in option]
                # value_found = options[0]
            time_counts += 1
        summary = self.SUMMARY_DEFAULT_MESSAGE \
            if summary is None else summary
        return summary, value_found

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
