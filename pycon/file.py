import sys

class File:
    "A utility to read royalty report."
    def __init__(self, name):
        self.name = name

    def openFile(self):
        the_sum = 0
        with open(self.name, 'r') as f:
            for line in f.readlines():
                usd = line.split("\t")[16].rstrip()
                try:
                    float_usd = float(usd)
                    the_sum += float_usd
                except Exception as e:
                    print e
                    pass
        return the_sum

    def __str__(self):
        return 'File: {0}'.format(self.name)
