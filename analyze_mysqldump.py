#!/usr/bin/env python

import os
import re
import sys

file = sys.argv[1]
print 'opening', file
f = open(file)

open_dump_files = set()

for line in f:
    #print line
    m = re.match('^INSERT INTO `(\S+)` VALUES \(', line)
    if m:
        dump_file = m.group(1) + '.txt'

        values = line.rstrip()[m.end(0):-2] #-2 to strip off trailing semicolon and closing paren
        value_array = values.split('),(')

        if dump_file in open_dump_files:
            fh = open(dump_file, 'a')
            print ' appending to', dump_file
        else:
            assert not os.path.exists(dump_file)
            fh = open(dump_file, 'w')
            print ' creating', dump_file
            open_dump_files.add(dump_file)

        for value in value_array:
            fh.write(value + '\n')

        fh.close()

print 'done'
