# LibreHand
A handy program for obtaining specified sequence(s) from multi-seq .fasta file. 

## Usage

Commandline options:

`Librehand <-y> -s filter1 <-s filter2 <-s ...>> -f filterfile file1 file2 file3...`

## Introduction

Target files could be pattern strings for globing.

Created on Thu Jun 28 21:10:14 2012 for LSC(李善策), MJF(马建飞), LBH(李博涵) and YSX(于淑贤).

This script was designed for LSC's work on evolution of ST&RM systems in
cyanobacteria. It can extract wanted fasta sequences from your target files
once you specify filter strings in the sequence annotarions.

Filters to specify can be one or more in command line, or inclued in a file,
or both.

Target files in fasta format can be specified as one or more glob patterns.

@author: Yin-Chu WANG

## Acknowledgements

Thanks for kind advices by LSC, MJF, LBH and YSX. 
