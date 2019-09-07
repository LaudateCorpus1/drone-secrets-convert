#!/usr/bin/env python3

import sys
import textwrap

import oyaml as yaml
from collections import OrderedDict

yaml.warnings({'YAMLLoadWarning': False})
f = open(sys.argv[1]).read()
x = list((yaml.load_all(f)))

secrets = {}

for i in x:
    if i['kind'] != "secret":
        step = OrderedDict(i)
        print('---')
        print(yaml.dump(step))
    else:
        secrets = i

for i in secrets['external_data']:
    secret = """
        ---
        kind: secret
        name: %s
        get:
          path: %s
          name: %s""" % (i, secrets['external_data'][i]['path'], i)
    print(textwrap.dedent(secret))
