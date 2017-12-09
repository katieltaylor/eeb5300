from Bio import SeqIO

unclassified_records_id = [ ]

from Bio import SeqIO
for seq_record in SeqIO.parse("unclassified_2.fasta", "fasta"):
    unclassified_records_id.append (seq_record.id + "\n")
    
with open ("unclassified_records_3.txt" , "w") as output:
	output.writelines(unclassified_records_id)
output.close