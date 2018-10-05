import sys
from Bio import SeqIO

FastaFile = open("Cyanothece sp. ATCC51142.txt", 'rU')

for rec in SeqIO.parse(FastaFile, 'fasta'):
    name = rec.id
    seq = rec.seq
    seqLen = len(rec)
    print (name, seqLen)

FastaFile.close()