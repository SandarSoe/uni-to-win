# -*- coding: utf-8 -*-

import re


def replace(input):

    output = input

    output = re.sub(u'\u1000', u'\u0075', output)#kagyi
    output = re.sub(u'\u1001', u'\u0063', output)#kha_kway

