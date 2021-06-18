import sys

inFile = open(sys.argv[1], 'r')
outFile = str(sys.argv[2])+'_Bowtie2_output.txt'
f = open(outFile, 'w+')
for line in inFile:
    lineSplit = line.split('\t')
    if lineSplit[1] == '0':
        if lineSplit[2] == 'CHROMOSOME_I': #may need to change depending on input format, reference used
            f.write('+'+'\t'+'CHROMOSOME_I'+'\t'+lineSplit[3]+'\t'+lineSplit[9]+'\n')
        elif lineSplit[2] == 'CHROMOSOME_II':
            f.write('+'+'\t'+'CHROMOSOME_II'+'\t'+lineSplit[3]+'\t'+lineSplit[9]+'\n')
        elif lineSplit[2] == 'CHROMOSOME_III':
            f.write('+'+'\t'+'CHROMOSOME_III'+'\t'+lineSplit[3]+'\t'+lineSplit[9]+'\n')
        elif lineSplit[2] == 'CHROMOSOME_IV':
            f.write('+'+'\t'+'CHROMOSOME_IV'+'\t'+lineSplit[3]+'\t'+lineSplit[9]+'\n')
        elif lineSplit[2] == 'CHROMOSOME_V':
            f.write('+'+'\t'+'CHROMOSOME_V'+'\t'+lineSplit[3]+'\t'+lineSplit[9]+'\n')
        elif lineSplit[2] == 'CHROMOSOME_X':
            f.write('+'+'\t'+'CHROMOSOME_X'+'\t'+lineSplit[3]+'\t'+lineSplit[9]+'\n')
    elif lineSplit[1] == '16':
        if lineSplit[2] == 'CHROMOSOME_I':
            f.write('-'+'\t'+'CHROMOSOME_I'+'\t'+lineSplit[3]+'\t'+lineSplit[9]+'\n')
        elif lineSplit[2] == 'CHROMOSOME_II':
            f.write('-'+'\t'+'CHROMOSOME_II'+'\t'+lineSplit[3]+'\t'+lineSplit[9]+'\n')
        elif lineSplit[2] == 'CHROMOSOME_III':
            f.write('-'+'\t'+'CHROMOSOME_III'+'\t'+lineSplit[3]+'\t'+lineSplit[9]+'\n')
        elif lineSplit[2] == 'CHROMOSOME_IV':
            f.write('-'+'\t'+'CHROMOSOME_IV'+'\t'+lineSplit[3]+'\t'+lineSplit[9]+'\n')
        elif lineSplit[2] == 'CHROMOSOME_V':
            f.write('-'+'\t'+'CHROMOSOME_V'+'\t'+lineSplit[3]+'\t'+lineSplit[9]+'\n')
        elif lineSplit[2] == 'CHROMOSOME_X':
            f.write('-'+'\t'+'CHROMOSOME_X'+'\t'+lineSplit[3]+'\t'+lineSplit[9]+'\n')
f.close()
