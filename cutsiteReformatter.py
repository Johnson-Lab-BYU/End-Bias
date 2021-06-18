import sys

#this program takes output from filterCutsites.py and re-formats the output so that each line specifies the chromosome.
x = open(sys.argv[1],'r')
output = str(sys.argv[2])
f = open(output, 'w')

for line in x:
    if line.startswith('>'):
        list = line
        currentChr = str(list[1]+list[2]+list[3]+list[4])
    else:
        list = line.split('\t')
        f.write(currentChr+'\t'+str(list[1])+'\t'+str(list[2]))

f.close()
