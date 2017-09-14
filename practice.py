#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:13:06 2017

@author: Katie
"""
###this script GC content


#opens the file and stores it in the variable fh
fh = open ("/Users/Katie/desktop/demo.fasta", "r")

#store lines from fh into list called lines
lines = fh.readlines()


#this counts the number of genes
NumLines = 0

for l in lines:
    if l[0]==">":
        NumLines = NumLines + 1
        
print (NumLines)


NumA = 0
NumG = 0
NumC = 0
NumT = 0
NumAGTC = 0

for l in lines:
    if l[0]!=">":
        for n in l:
            if n == "A":
                NumA = NumA + 1
                NumAGTC = NumAGTC + 1
            if n == "G":
                NumG = NumG + 1
                NumAGTC = NumAGTC + 1
            if n == "C":
                NumC = NumC + 1
                NumAGTC = NumAGTC + 1
            if n == "T":
                NumT = NumT + 1
                NumAGTC = NumAGTC + 1
                
print (NumA, NumG, NumC, NumT, NumAGTC)
        
GC =  (NumG + NumC) / float(NumAGTC)
print (GC)            
