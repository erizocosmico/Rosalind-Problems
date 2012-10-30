#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("rosalind_revc.txt", 'r') as dataset:
        print dataset.readline()[::-1].replace("T", "X").replace("G", "W").replace("A", "T").replace("C", "G").replace("X", "A").replace("W", "C")

if __name__ == "__main__":
	main()