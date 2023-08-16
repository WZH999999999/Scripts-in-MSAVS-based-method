import pysam as sam
import pandas as pd
import re
fasta=sam.FastaFile(r"path/of/the/sequences/to/be/tested")
wzh=[]
for i in fasta.references:
    s=fasta.fetch(i)
    if len(re.findall('X',s))>0:
        wzh.append(i)
len(wzh) #Check the number of sequences containing “X”
#Remove the sequences containing “X” and output the fasta file after removing the unqualified sequences.
f=open(r"the/path/to/the/new/generated/fasta/file","w")
for i in fasta.references:
    if i not in wzh:
        print(">%s"%i,'\n',fasta.fetch(i),file=f)
f.close()
