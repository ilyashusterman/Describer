import argparse
import logging
from unipath import Path

from describers.Recognition import Recognition
from describers.Search import Search


class Description(object):

    def __init__(self, image):
        self.filename = image

    def describe(self):
        recognition = Recognition(Path(Path(__file__).parent,
                                       self.filename))
        classification = recognition.classify_image()
        search = Search(classification['value'])
        analization = search.get_analyzization(sentences=2)
        description = {
            'value': search.keyword,
            'data': analization['summary']
        }
        # print('Value={}'.format(search.keyword))
        # print('Data={}'.format(analization['summary']))
        print('description={}'.format(description))

    @classmethod
    def main(cls):
        parser = argparse.ArgumentParser()
        commands = parser.add_mutually_exclusive_group(required=True)
        commands.add_argument('--describe', action='store_true')
        parser.add_argument('--image', default='test.jpg',
                            help='Custom input test image default test.jpg')
        args = parser.parse_args()
        describer = cls(args.image)
        if args.describe:
            describer.describe()
        elif args.insert:
            raise NotImplementedError()
        else:
            logging.info('Nothing to do.')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    Description.main()
