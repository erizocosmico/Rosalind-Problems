#!/usr/bin/env python

from itertools import permutations

with open("rosalind_perm.txt", 'r') as f:
    n = int(f.readline())
    perms = list(permutations([i for i in range(1, n + 1)], n))
    with open("rosalind_perm_result.txt", 'w') as fw:
        fw.write(str(len(perms)) + "\n")
        for perm in perms:
            pstr = ""
            for p in perm:
                pstr += str(p) + " "
            fw.write(pstr.rstrip() + "\n")