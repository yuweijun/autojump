# -*- coding: utf-8 -*-
from collections import namedtuple


class Version(namedtuple('Version', ['major', 'minor', 'micro'])):

    def __str__(self):
        return '%s.%s.%s' % (self.major, self.minor, self.micro)


version = Version(22, 3, 3)
