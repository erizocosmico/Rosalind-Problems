#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("rosalind_gc.txt", 'r') as f:
        (curr_tag, max_tag) = ("", "")
        curr_str = ""
        (curr_percent, max_percent) = (0.0, 0.0)
        for line in f.readlines():
            if ">" in line:
                if curr_tag != "" and curr_str != "":
                    curr_percent += sum([1 for i in curr_str if i in ['G', 'C']]) / float(len(curr_str)) * 100.0
                    if curr_percent > max_percent:
                        max_tag = curr_tag
                        max_percent = curr_percent
                    curr_percent = 0.0
                    curr_str = ""
                curr_tag = line.replace(">", "").replace("\n", "")
            else:
                curr_str += line.replace("\n", "")
        curr_percent += sum([1 for i in curr_str if i in ['G', 'C']]) / float(len(curr_str)) * 100.0
        if curr_percent > max_percent:
            max_tag = curr_tag
            max_percent = curr_percent
        print "%s\n%f%%" % (max_tag, max_percent)

if __name__ == "__main__":
	main()