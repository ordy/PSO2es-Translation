#!/usr/bin/env python3
# coding=utf8
import codecs
import fnmatch
import os
import json
import sys

counterr = 0
invalid_json_files = []

if len(sys.argv) < 2:
    sys.exit(os.EX_NOINPUT)

dir = sys.argv[1]

json_files = [
    os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(dir)
    for f in fnmatch.filter(files, '*.txt')
]
for files in json_files:
    with codecs.open(files, mode='r', encoding='utf-8') as json_file:
        try:
            countin = 0
            djson = json.load(json_file)
            for rmid in djson:
                countin += 1
            if (countin == 0):
                print("%s: %s") % (files, "BLANK")
                invalid_json_files.append(files)
        except ValueError as e:
            print("%s: %s" % (files, e))
            invalid_json_files.append(files)

counterr += len(invalid_json_files)
if counterr != 0:
    sys.exit("=============\nJSON files with issues: %d" % counterr)
