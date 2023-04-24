#!/usr/bin/env python3

import string
import time

alph = list(string.printable)
s = str(input('Enter anything printable: '))
r = ''

# time.sleep(5)

for i in range(len(s)):
    for a in alph:
        r += a
        time.sleep(0.01)
        print(r)
        if r[-1] == s[i]:
            break
        r = r[:-1]
