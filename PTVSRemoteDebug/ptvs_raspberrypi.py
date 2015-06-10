# -*- coding: utf-8 -*-

import ptvsd
import platform

ptvsd.enable_attach(secret = 'thinkAmi')

os = platform.system()

print u'ここでアタッチを待ちます'

if os != 'Windows':
    ptvsd.wait_for_attach()

print u'platform.systemの結果は %s です' % os