from distutils.debug import DEBUG
import logging

class Log:
    def __init__(self):
        self.padrao = logging.basicConfig(filename='/scripts/backup.log',
        format='%(message)s %(asctime)s',
        filemode='a',
        encoding='utf-8',
        level=DEBUG)

nota = Log()