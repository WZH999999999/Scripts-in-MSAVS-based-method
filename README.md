# Scripts-in-MSAVS-based-method
The scripts used in a novel MSA-VS based approach (for conservative epitopes filtering to boost vaccines design against SARS-CoV-2 mutations).

### 1. A python script that extract the earliest uploaded Pango lineage and its corresponding information from the original data list with the same Pango lineage.
**Function:** After getting the sequence download summary table from NCBI database, use python script below to keep the unique value in the same Pango lineage (keep the download information of the earliest uploaded sequence in the same Pango lineage) and output the new sequence download list.

**Usage:** Open the Jupyter notebook and run the **code 1**.

### 2. A shell script based on Entrez Direct (https://www.ncbi.nlm.nih.gov/books/NBK179288/) for batch sequence downloading (sequence_batch_download.sh).
**Function:** Batch download sequences based on their IDs.

**Usage:** Place the text format of the ID (accession number) list in a folder, past the script in the same folder, then run the following bash script at the Linux command line.
> bash Sequence_batch_download.sh IDlist.txt #database #outputname

### 3. A python script used for searching unqualified sequences in the downloaded sequences.
**Function:** Search for unqualified sequences containing “X” in the downloaded sequences, and output the fasta file after removing the unqualified sequences.

**Usage:** Open the Jupyter notebook and run the following **code 2**.

### 4. A shell script used for virtual screening (Batch_docking.sh).
**Function:** Batch molecular docking based on AutoDock Vina.

**Usage:** Place the pdbqt file, config file and IDlist file used for molecular docking in the same folder, run the following bash script for batch docking (docking each epitope in turn with all antibodies in this folder), and collate the best docking results from each molecular docking in the result.csv file.
> bash Batch_docking.sh #LigandnamelistID ReceptornamelistID
