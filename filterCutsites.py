import sys
#This program filters out DNA fragments smaller than 147 bp and removes their
#fragment start & stop from the master file, creating a new tab delimited file.  
x = open(sys.argv[1], 'r')
output = str(sys.argv[2])
f = open(output, 'w')

for line in x:
    if line.startswith(">"):
        f.write(line)
    else:
        line = line.split('\t')
        if int(line[2]) - int(line[1]) >= 147:
            f.write(str(line[0])+'\t'+str(line[1])+'\t'+str(line[2])+'\n')
        else:
            continue

f.close()
