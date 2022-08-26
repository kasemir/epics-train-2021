#!/bin/env python3

from channelfinder import ChannelFinderClient
cf = ChannelFinderClient()
for c in cf.find(name='*TMP*'):
    print(c['name'])

