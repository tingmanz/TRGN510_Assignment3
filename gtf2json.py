
#!/usr/bin/python

import sys
import json

file_name = sys.argv[1]
gene_list = []
with open(file_name, 'r') as file:
    for line in file:
        if not line.startswith('#'):
            elements = line.split("\t")
            if elements[2] == 'gene':
                gene_dict = {}
                info_list = elements[8].split("\"")
                gene_dict['geneName'] = info_list[3]
                gene_dict['chr'] = elements[0]
                gene_dict['startPos'] = elements[3]
                gene_dict['endPos'] = elements[4]
                gene_list.append(gene_dict)
with open('gene.json', 'w') as file:
    json.dump(gene_list, file)
