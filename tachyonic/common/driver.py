from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from tachyonic.neutrino.utils.general import import_module

log = logging.getLogger(__name__)

def get_driver(driver):
    ds = driver.split('.')
    l = len(ds)
    d = ds[l-1]
    m = ".".join(ds[0:l-1])
    module = import_module(m)
    driver = getattr(module, d)
    return driver
