import operator
from collections import Counter
from describers.classify_image import get_image_classification


class Recognition(object):
    DEFAULT_BEST_SCORE = 0.55

    def __init__(self, filename):
        self.filename = filename

    def classify_image(self):
        classifications = get_image_classification(self.filename)
        print(classifications)
        max_key = max(classifications.keys(), key=float)
        if max_key > self.DEFAULT_BEST_SCORE:
            print('max_key={}'.format(max_key))
            return classifications[max_key]
        else:
            keys_values = [sentences['value']
                           for key, sentences in classifications.items()]
            print ('keys_values={}'.format(keys_values))
            keys = self.find_keyword(keys_values)
            print('keys={}'.format(keys))
            max_count_key = max(keys.items(), key=operator.itemgetter(1))
            print('max_count_key={}'.format(max_count_key[0]))
            return {'value': max_count_key[0]}

    def find_keyword(self, keywords):
        words = []
        for keyword in keywords:
            sentence = str(keyword).split()
            sentence = self.get_common_keys_in_sentence(sentence)
            words += sentence
        return dict(Counter(words))

    def get_common_keys_in_sentence(self, sentence):
        new_words = []
        words = sentence
        for word in words:
            for second_word in words:
                if word in second_word:
                    if word is second_word:
                        pass
                    else:
                        new_words.append(second_word.replace(word,
                                                             '').replace(',', ''))
        new_words = [char for char in new_words if char != '']
        all_words = words+new_words
        return all_words
