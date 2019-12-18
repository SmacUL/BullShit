import os.path as op
import os


class File:

    def __init__(self):
        pass

    @staticmethod
    def read_file(path):
        with open(path) as file:
            return file.readlines()

    @staticmethod
    def write_file(path, article):
        if not op.exists(op.dirname(path)):
            os.mkdir(op.dirname(path))

        with open(path, mode='w') as file:
            file.write(article)
