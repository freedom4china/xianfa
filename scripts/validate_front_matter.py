#!/usr/bin/env python3
import os
import re
import sys

# Simple front-matter id uniqueness validator
# Scans constitution/ and proposals/ for YAML front-matter 'id:' fields and reports duplicates.

def find_ids_in_file(path):
    ids = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        return ids
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return ids
    body = m.group(1)
    # find id: value
    for line in body.split('\n'):
        if line.strip().startswith('id:'):
            parts = line.split(':',1)
            if len(parts) > 1:
                ids.append(parts[1].strip())
    return ids

base_dirs = ['constitution', 'proposals']
all_ids = {}
errors = False
for base in base_dirs:
    if not os.path.isdir(base):
        continue
    for root,_,files in os.walk(base):
        for fn in files:
            if not fn.endswith('.md'):
                continue
            path = os.path.join(root,fn)
            ids = find_ids_in_file(path)
            for idv in ids:
                if not idv:
                    print(f"WARNING: file {path} has empty id in front-matter")
                    errors = True
                    continue
                if idv in all_ids:
                    print(f"ERROR: duplicate id '{idv}' found in {path} and {all_ids[idv]}")
                    errors = True
                else:
                    all_ids[idv] = path

if errors:
    print('\nFront-matter validation failed.')
    sys.exit(2)
else:
    print('Front-matter validation passed. IDs found:')
    for k,v in all_ids.items():
        print(f"  {k} -> {v}")
    sys.exit(0)