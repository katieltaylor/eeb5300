##Coding Challenge 1

##### PROBLEM 1

#opens the file and stores it in the variable fh
kt = open ("/Users/Katie/desktop/5300/Challenge1/PitaIlluminaGeneSet.fasta", "r")

#store lines from fh into list called lines
lines = kt.readlines()


##### PROBLEM 2

##sets numgenes equal to zero
numgenes = 0

##checks if first character in line is > symbol, 
####if so adds 1 to the total gene count
for l in lines:
    if l[0]==">":
        numgenes = numgenes + 1
        
##prints the number of genes counted by starting with > symbol
print (numgenes)



##### PROBLEM 3

###makes empty lists called SeqNames and Sequences

SeqNames = [ ]
Sequences = [ ]

####checks if first character in line is not > symbol, if not appends line
### to the new sequences list 
for l in lines:
    if l[0]!=">":
        Sequences.append (l)
        
####checks if first character in line is > symbol, if so appends line
### to the new seqnames list 
        
for l in lines:
    if l[0]==">":
        SeqNames.append (l)

####makes empty list called seqlen and adds the lenght of each sequence to it

SeqLen = [ ]

for l in Sequences:
    SeqLen.append (len(l))
    
 ####records the index for the shortest sequence, then prints the name and length of that sequence 
lowindex = (SeqLen.index(min (SeqLen)))

print (SeqNames[lowindex])
print (SeqLen[lowindex])

 ####records the index for the longest sequence, then prints the name and length of that sequence
highindex = (SeqLen.index(max (SeqLen)))

print (SeqNames[highindex])
print (SeqLen[highindex])


#####Calculates the average by taking the sum of list items and dividing by length of list

sum(SeqLen)/float(len(SeqLen))


######PROBLEM 4
indexlist = [ ]
indexlist2 = [ ] 

for l in SeqLen:
    if l < 500:
        indexlist.append (l)
    
for i in indexlist:
    indexlist2.append (SeqLen.index (i))

###make and open a new file called output
h = open ("output.txt" , "w")
    

## make a list called r and add name and sequences matching index of len <500
r = [ ]

for i in indexlist2:
    r.append (SeqNames [i])
    r.append (Sequences [i])
    
###write all the lines in list r to output file
h.writelines(r)

h.close
        
