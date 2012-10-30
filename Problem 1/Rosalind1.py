#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	(a, c, g, t) = (0, 0, 0, 0)
	with open("rosalind_dna.txt", 'r') as f:
            for char in f.readline():
                if char == "A":
                    a += 1
                else:
                    if char == "C":
                        c += 1
                    else:
                        if char == "G":
                            g += 1
                        else:
                            if char == "T":
                                t += 1
            print "%d %d %d %d" % (a, c, g, t)

if __name__ == "__main__":
    main()