from Bio import SeqIO

##Problem 1
SeqList=list(SeqIO.parse("Adarlingi_v1.fna", "fasta"))

###### Problem 2
with open ("Adarlingi_v1.gff", "r") as gff:
    GFFLines = gff.readlines()

with open("genes.txt", "r") as genes:
    GeneList = genes.readlines()

Chromosome = [ ]
Name = [ ]
Start = [ ]
Stop = [ ]
Strand = [ ]
genelist2 = [ ]
genelist = [ ]

for gene in GeneList:
    genelist1 = gene.split("\n")
    genelist2.append (genelist1)
for gene in genelist2:
    genelist.append (gene[0])
    
import re
for record in GFFLines:
    if record[0] != "#":
        column = record.split("\t")
        if column[2] == "gene":
            names = re.split("Name=|;",column[8])
            if names[2] in genelist:
                Chromosome.append (column[0])
                Start.append (column[3])
                Stop.append (column[4])
                Name.append (names[2])
                Strand.append (column[6])
 
print (len(Chromosome)) 
print (len (Start))          
print (len (Stop))
print (len (Name))
print (len (Strand))

###### Problem 3

record_dict = SeqIO.index("Adarlingi_v1.fna", "fasta")

gatacount=0

for chr , sta, std in zip (Chromosome, Start, Strand):
    sequence = record_dict[chr]
    promotorstart = int(sta) - 501
    promotor = sequence.seq[int(promotorstart):int(sta)]
    upperpromotor = promotor.upper()
    if std == "+":
    	if "GATA" in upperpromotor:
    		gatacount = gatacount+1
    elif std == "-":
    	if "TATC" in upperpromotor:
    		gatacount = gatacount+1

print (gatacount)
    
######### Problem 4

writer = [ ]

for c , sta, stp, std, nm in zip (Chromosome, Start, Stop, Strand, Name):
    sequence = record_dict[chr]
    promotorstart = int(sta) - 501
    promotor = sequence.seq[int(promotorstart):(int(sta)-1)]
    gene = sequence.seq[(int(sta)-1):(int(stp)-1)]
    upperpromotor = promotor.upper()
    if std == "+":
    	if "GATA" in upperpromotor:
    		writer.append(str(nm))
    		writer.append(str(promotor))
    		writer.append(str(gene))
    if std == "-":
    	if "TATC" in upperpromotor:
    	        writer.append(str(nm))
    		writer.append(str(promotor))
    		writer.append(str(gene))
    		 	
with open ("output.fasta" , "w") as output:
	output.writelines(str(writer))
output.close
 
