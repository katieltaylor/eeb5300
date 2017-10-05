#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:23:39 2017

@author: Katie
"""

#######Problem 1

#opens the file and stores it in the variable kt
kt = open ("/Users/Katie/desktop/5300/Challenge2/Pita_MakerAlignments.gff3", "r")

#store lines from kt into list called gfflines
gfflines = kt.readlines()

genecount = 0

#goes through gfflines, if it isnt a comment and the third column says gene 
#it adds one to the genecount
for l in gfflines:
    if l[0] != "#" :
        column=l.split("\t")
        if column[2] == "gene" :
            genecount = genecount+1

print (genecount)


#######Problem 2

genelist = [ ]

#makes a list of gene names called genelist from the last column from each line that has gene 
#identifer in the third column
import re
for l in gfflines:
    if l[0] != "#" :
        column=l.split("\t")
        if column[2] == "gene":
            names=re.split(";|\n",l)
            genelist.append(names[1])


exoncount = [ ]
excounter = 0     
 
#iterates through genelist, if in split gfflines ID column is name in gene list
#and column 3 says exon, adds one to the excounter. Then it appends number of exons for each
#gene held in variable excounter to exoncount list. Then resets excounter to zero for next gene

for g in genelist:
    for l in gfflines:
        if l[0] != "#" :
            column=l.split("\t")
            if g in column[8] and column[2] == "exon":
                excounter = excounter+1
    exoncount.append(excounter)
    excounter = 0 


multicounter = 0
monocounter = 0

#goes through exoncount. If count is equal to one it adds one to the monocounter total
for g in exoncount:
    if g == 1:
        monocounter = monocounter+1
        
print (monocounter)

#goes through exoncount. If count is not equal to one it one to the multicounter total
for g in exoncount:
    if g != 1:
        multicounter = multicounter+1
        
print (multicounter)

####### Problem 4

exonlengths= [ ]

# adds the difference between exon start and stop points to list of exonlenghts
for l in gfflines:
    if l[0] != "#" :
        column=l.split("\t")
        if column[2] == "exon":
            exonlengths.append(int(column[4]) - int(column[3]))
            
#prints summary information about exon lengths
print (min(exonlengths))
print (max (exonlengths))
print (sum(exonlengths)/float(len(exonlengths)))
import statistics
print (statistics.median(exonlengths))


##### Problem 5
h = open ("finaloutput.gff3" , "w")

r = [ ]

multigenelist = [ ]

#extracts the list of multiexonic gene names
for (g, e) in zip (genelist, exoncount):
    if e != 1:
        multigenelist.append(g)

#moves all data for multiexonic genes to new list        
for m in multigenelist:
    for l in gfflines:
        if l[0] != "#" :
            column=l.split("\t")
            if m in column[8]:
                r.append(l)

## removes any lines that are exons and shorter than 19                
for q in r:
    columns=q.split ("\t")
    if columns[2] == "exon" and ((int(columns[4]) - int(columns[3]))) > 20:
        r.remove(q)

    
h.writelines(r)

h.close
 

