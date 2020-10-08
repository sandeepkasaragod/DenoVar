import read_file
import tryptic_peptide
import os
import re
import sys
from itertools import islice
import pandas as pd

def distance(a, b):
    f = (lambda x, y: 0 if x == y else 1)
    return sum(map(f, a, b))

def normal_seq():
        rds = read_file.read_fasta(prot_db_cleave)
        for rows in rds:
            dict_seq[rows[0].split('|')[3]] = rows[1].rstrip()

def get_variant_aa_pos(variant_pep, normal_pep, acc): #For getting the genome locationl
    normal_seq = dict_seq[acc]
    variant_pos = [(x, variant_pep[x]) for x in range(len(variant_pep)) if variant_pep[x] != normal_pep[x]]
    position = int(normal_seq.index(normal_pep)) + int(variant_pos[0][0])
    return normal_seq[position], position + 1, variant_pos[0][1]  #print (position, normal_seq[position])
