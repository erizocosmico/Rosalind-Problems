#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("rosalind_rna.txt", 'r') as dataset:
        print "".join([char if char != 'T' else 'U' for char in dataset.readline()])
    
if __name__ == "__main__":
    main()