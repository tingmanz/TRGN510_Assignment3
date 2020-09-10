#!/usr/bin/python

import sys
import fileinput
import re

file_name = sys.argv[1]
with open(file_name, 'r') as file:
    for line in file:
        area_code = re.findall(r'^(\(\d{3})', line)
        print(area_code[0][1:])
