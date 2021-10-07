# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:34:25 2012

@author: Administrator
"""

from Bio import SeqIO

def filterdup(bseq="ab.fasta", seqformat="fasta"):
    bigrecords = SeqIO.parse(bseq, seqformat)
    a= list(bigrecords)
    #print a
    sites= []
    for aseq in a:
        #print aseq
        if aseq.id not in sites:
            #print "Hello,",aseq.id
            sites.append(aseq.id)
            print aseq.format("fasta")
            #print sites
           
        #else:
            #print "Found duplicates:", aseq.id
    return len(a),len(sites)
            
            
filterdup("stations_sequences.fasta")
            
    
