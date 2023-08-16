#!usr/bin/bash
epitopename=$(cat $1)
receptor=$(cat $2)
for i in $epitopename
do
        for j in $receptor
        do
                qvina2.1 --ligand $i".pdbqt" --receptor $j".pdbqt" --config $j"_config.txt" --exhaustiveness=24 --seed 0 --out $i"+"$j"_dockingresult.pdbqt" --log $i"+"$j"dockinglog.log"
                score=$(cat $i"+"$j"_dockingresult.pdbqt"|awk "NR==2"|awk '{print $4}')
                echo "$i,$j,$score" >> results.csv
        done
done
