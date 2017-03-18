from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from tachyonic.neutrino import exceptions
from tachyonic.neutrino import constants as const

log = logging.getLogger(__name__)


class Error(exceptions.Error):
    def __init__(self, description):
        Exception.__init__(self, description)
        self.description = description

    def __str__(self):
        return str(self.description)


class Authentication(Error):
    def __init__(self, description):
        Exception.__init__(self, description)
        self.description = description

    def __str__(self):
        return str(self.description)
