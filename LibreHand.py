# -*- coding: utf-8 -*-

MSG = """

%prog <-y> -s filter1 <-s filter2 <-s ...>> -f filterfile file1 file2 file3...

Target files could be pattern strings for globing.

Created on Thu Jun 28 21:10:14 2012 for LSC, MJF, LBH and YSX. 

This script was designed for LSC's work on evolution of ST&RM systems in
cyanobacteria. It can extract wanted fasta sequences from your target files
once you specify filter strings in the sequence annotarions. 

Filters to specify can be one or more in command line, or inclued in a file, 
or both.

Target files in fasta format can be specified as one or more glob patterns.

@author: Yin-Chu WANG
yinchu.wang@gmail.com

"""

from optparse import OptionParser
import glob
from Bio import SeqIO

#MSG='''%prog -x -s filter1 -s filter2 -s ... -f filterfile file1 file2 file3...
#    target files could be the string for globing.'''

op=OptionParser(usage=MSG, \
                version="%prog 4.0 by YC Wang")

op.add_option("-y", '--yield', action="store_true", dest="cut", help="If you wanna cut from the files." )

op.add_option("-g", '--group', action="store_true", dest="group", help="If you wanna group sequences by filters." )

op.add_option("-s", "--sig", action="append", dest="filterS", help="Give your one or more filter strings for extration.")

op.add_option("-f", "--filters", action="store", dest="filterF", help="Give your fiters inclued in a file")


options, targets = op.parse_args()

# Given all the target files you want, every parameter can be a glob string.
def getglobfiles(targetfiles):
    globfiles=[]
    for f  in targetfiles:
        add= glob.glob(f)
        globfiles += add
    return globfiles

def getfilters(filterstr, filterfile):
    filters= []
    if filterfile != None:
        with open(filterfile) as ff:
            for i in ff.readlines():
                filters.append(i.strip()) 
    if filterstr != None:
        filters.extend(filterstr)
    return filters

# extract every satifised sequence from one targer file to a new file
# prefixed X_ and the rest sequences  are left in the other new file
# which prefixed Y_.  
def targetfilter(filters, targetfile, xymode, gmode):
    newx = 0
    newy = 0
    xhandle = open('X_'+targetfile, "a")
    if xymode == True:
        yhandle = open('Y_'+targetfile, "a")
    if gmode == True:
        flthandle = dict()
        for flt in filters:
            flthandle[flt] = open('G_'+flt, "a")
    records = SeqIO.parse(targetfile, "fasta")
    
    for record in records:
        isfound = 0
        for flt in filters:
            if flt in record.description:
                isfound = 1
                if gmode == True:
                    SeqIO.write(record, flthandle[flt], "fasta")
        if isfound == 1:
            newx += 1
            SeqIO.write(record, xhandle, "fasta")
        else:
            newy += 1
            if xymode == True:
                SeqIO.write(record, yhandle, "fasta")
            
    print '%s has been processed, %d found(X) and %d left(Y).'%(targetfile, newx, newy)
    #print xymode

def main(filters, targetfiles, xymode, gmode):
    for targetfile in targetfiles:
        targetfilter(filters, targetfile, xymode, gmode)
    print 'A total number of %d files have been processed successfully! ;)'%(len(targetfiles))             


# Go ahead, baby~
filters = getfilters(options.filterS, options.filterF)
targetfiles = getglobfiles(targets)
xymode = options.cut
gmode  = options.group
#print xymode
main(filters, targetfiles, xymode, gmode)