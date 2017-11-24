import wikipedia
#wikipedia.wikipedia.API_URL='http://en.citizendium.org/api.php'

class Searcher(object):
    def __init__(self, keyword):
        self.keyword = keyword

    def get_analyzization(self):
        found_pages = wikipedia.search(self.keyword)
        if len(found_pages) > 0:
            # FIXME better way to foind out
            value_found = found_pages[0]
            assert value_found == self.keyword.title()
        else:
            return {'name': 'no_information'}
        # value_meta = wikipedia.page(value_found)
        summary = wikipedia.summary(value_found, sentences=2)
        return {
            'name': value_found.lower(),
            'summary': summary
        }
