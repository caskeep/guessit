#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
size property
"""
import re

from rebulk import Rebulk

from ..common import dash
from ..common.quantity import Quantity
from ..common.validators import seps_surround


def size():
    """
    Builder for rebulk object.
    :return: Created Rebulk object
    :rtype: Rebulk
    """
    rebulk = Rebulk().regex_defaults(flags=re.IGNORECASE, abbreviations=[dash])
    rebulk.defaults(name='size', validator=seps_surround)
    rebulk.regex(r'\d+\.?[mgt]b', r'\d+\.\d+[mgt]b', formatter=Quantity.fromstring, tags=['release-group-prefix'])

    return rebulk
