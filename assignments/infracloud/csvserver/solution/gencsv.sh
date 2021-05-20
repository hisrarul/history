INTERATIONS=10
for i in $(seq $INTERATIONS); do echo $(expr $i - 1), $(shuf -i 1-1000 -n1) | tee -a inputFile; done