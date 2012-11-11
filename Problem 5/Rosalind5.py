#!/usr/bin/env python
# -*- coding: utf8 -*-

with open("rosalind_hamm.txt", 'r') as f:
    strings = []
    for s in f.readlines():
        strings.append(s)
    print sum([1 for pos in xrange(0, len(strings[0]) - 1) if strings[0][pos] != strings[1][pos]])   
        