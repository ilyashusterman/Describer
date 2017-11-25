import operator

from describers.classify_image import get_image_classification


class Recognition(object):
    def __init__(self, filename):
        self.filename = filename

    def classify_image(self):
        classifications = get_image_classification(self.filename)
        print (classifications)
        max_key = max(classifications.keys(), key=float)
        print(max_key)
        return classifications[max_key]
