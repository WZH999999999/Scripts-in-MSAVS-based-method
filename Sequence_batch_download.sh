#!usr/bin/bash
#exemplehere: bash sequence_batch_download.sh unipangolin_surfaceprotein_ID.txt protein surfaceprotein 

IDpath=$1
database=$2
outputname=$3
ID=$(cat $IDpath)
for i in $ID
do
        efetch -db $database -id ${i} -format fasta >> $outputname.fasta
done
