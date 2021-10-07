# -*- coding: utf-8 -*-
"""
自动读入newick文件，提取OTU名称，并按次名称筛选序列

"""

import re
import string
from Bio import SeqIO

def subtree_leaves(treefile):
    with open(treefile, 'r') as treehandle:
        tree =  treehandle.read()
        leaf_pat = re.compile(r"(?: ,\(? ) .*? (?: \: )", re.X)
        raw_leaves = leaf_pat.findall(tree)
        #print raw_leaves
        table = string.maketrans('','')
        leaves =  [leaf.translate(table, ',(:') for leaf in raw_leaves]
        for leaf in leaves:
            print leaf
            
def fastafilter(dbfasta, leaves, m="x"):
    sub1= dbfasta+'here'
    sub2= dbfasta+'rest'
    with open(dbfasta, "r") as db:
        if m=="c":
            with open(sub1, 'a') as h1:                        
                for seq in SeqIO.parse(db, "fasta"):
                    if seq.description in leaves:                        
                        SeqIO.write(seq, h1, "fasta")
                        
        elif m=="d":
            with open(sub1, 'a') as h2:                        
                for seq in SeqIO.parse(db, "fasta"):
                    if seq.description not in leaves:                        
                        SeqIO.write(seq, h2, "fasta")

        else:
            with open(sub1, 'a') as h1, open(sub2, 'a') as h2:                        
                for seq in SeqIO.parse(db, "fasta"):
                    if seq.description in leaves:                        
                        SeqIO.write(seq, h1, "fasta")
                    else:
                        SeqIO.write(seq, h2, "fasta")
                        
    print 'Sequences successfully filtered!'
    