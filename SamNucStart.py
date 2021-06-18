import sys
import random

#This program is create a SAM file based on output from the RescueAndDyadCalling.jar and UnknownEndsDyadCalling.jar java 
#programs.  This was used to create nucleosome start SAM files.  Output can be used in SAMtools to create BAM files.  
#Subsequent BAM files were used by tools in the deepTools suite.

colin_file = open(sys.argv[1], 'r')

read_name_count = 0

x = int(sys.argv[3]) #integer is read length

colin_read = colin_file.readlines()
sam_file = str(sys.argv[2])+'.sam'

with open(sam_file, 'w') as f:
    for item in colin_read:
        read_name_count += 1
        split = item.split('\t')
        if str(split[0]) == 'chr1':
            currentChr = 'chrI'
        elif str(split[0]) == 'chr2':
            currentChr = 'chrII'
        elif str(split[0]) == 'chr3':
            currentChr = 'chrIII'
        elif str(split[0]) == 'chr4':
            currentChr = 'chrIV'
        elif str(split[0]) == 'chr5':
            currentChr = 'chrV'
        elif str(split[0]) == 'chrX':
            currentChr = 'chrX'
        else:
            continue
        f.write('ilovecats'+str(random.randint(0,1000000))+str(read_name_count)+'\t'+str(0)+'\t'+currentChr+'\t'+str(int(split[1])-74)+'\t'+str(42)+'\t'+str(x)+'M'+'\t'+'*'+'\t'+str(0)+'\t'+str(0)+'\t'+'*'+'\t'+'*'+'\n')

f.close()
