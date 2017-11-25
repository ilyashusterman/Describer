import wikipedia
from plugins.citizendium import citizendium


class Search(object):
    def __init__(self, keyword):
        self.keyword = keyword

    def get_analyzization(self):
        # citi_found_pages = citizendium.search(self.keyword)
        found_pages = wikipedia.search(self.keyword)
        if len(found_pages) > 0:
            # FIXME better way to foind out
            value_found = found_pages[0]
            # citi_value_found = citi_found_pages[0]
            assert value_found == self.keyword.title()
        else:
            return {'name': 'no_information'}
        # value_meta = wikipedia.page(value_found)
        summary = wikipedia.summary(value_found, sentences=2)
        # summary_city = citizendium.summary('Dog', sentences=2)

        return {
            'name': value_found.lower(),
            'summary': str(summary),
            # 'summary_city': summary_city
        }
