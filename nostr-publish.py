#!/usr/bin/env python3

import sys
from common import connect_to_relays, disconnect_from_relays, publish_note

if len(sys.argv) < 3 or sys.argv[1] == '-h' or sys.argv[1] == '-?' or sys.argv[1] == '--help':
    print('Usage: ' + sys.argv[0] + ' nsec message')
    sys.exit(1)

connect_to_relays()
publish_note(sys.argv[1], sys.argv[2])
disconnect_from_relays()
