#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG)

###################################################
#  StringIO: 在内存中读写str
###################################################
from io import StringIO
with StringIO() as f:
    f.write('Hi')
    f.write(' ')
    f.write('Simeon Qi')
    logging.info(f.getvalue())


###################################################
#  BytesIO: 在内存中读写二级制
###################################################
from io import BytesIO
with BytesIO() as f:
    f.write('abc中文'.encode('utf-8'))
    logging.info(f.getvalue())
