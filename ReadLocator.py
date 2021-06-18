import sys

#This program is designed to take two SAM files and generate a 2x2 table to look at the number of reads at a given location in contrast to all other reads.  
#This program can be run on any position, but is designed to use a fragment length file as one of the input files.

z = int(sys.argv[4]) #distance from cutsite i.e. distance from ends
output = str(sys.argv[5]) #name of output
file = open(output, 'w')

sites1 = []  #separate cutsite location file into modified location lists by chromosome using user-defined distance from fragment ends
sites2 = []  #argument 1
sites3 = []
sites4 = []
sites5 = []
sitesX = []
test = []

#empty variables with count data for now, will be used for output file
c = 0 #reads at user defined position, Sample A or argument 2
d = 0 #remaining reads, Sample A or argument 2
e = 0 #reads at user defined position, Sample B or argument 3
f = 0 #remaining reads, Sammple B or argument 3

#separate cutsite file into list of modified location lists by chromosome using user-defined distance from fragment ends
with open(sys.argv[1], 'rt') as x:
    for line in x:
        if line.startswith('chr1') or line.startswith('chrI'):
            line = line.split()
            a = int(line[1]) + int(z)
            b = int(line[2]) - int(z)
            sites1.append(a)
            sites1.append(b)
        elif line.startswith('chr2') or line.startswith('chrII'):
            line = line.split()
            a = int(line[1]) + int(z)
            b = int(line[2]) - int(z)
            sites2.append(a)
            sites2.append(b)
        elif line.startswith('chr3') or line.startswith('chrIII'):
            line = line.split()
            a = int(line[1]) + int(z)
            b = int(line[2]) - int(z)
            sites3.append(a)
            sites3.append(b)
        elif line.startswith('chr4') or line.startswith('chrIV'):
            line = line.split()
            a = int(line[1]) + int(z)
            b = int(line[2]) - int(z)
            sites4.append(a)
            sites4.append(b)
        elif line.startswith('chr5') or line.startswith('chrV'):
            line = line.split()
            a = int(line[1]) + int(z)
            b = int(line[2]) - int(z)
            sites5.append(a)
            sites5.append(b)
        elif line.startswith('chrX'):
            line = line.split()
            a = int(line[1]) + int(z)
            b = int(line[2]) - int(z)
            sitesX.append(a)
            sitesX.append(b)
        else:
            continue

#generate count data for variables c and d defined earlier using nucleosome start SAM file as input
with open(sys.argv[2], 'rt') as x:
    for line in x:
        if line.startswith('@'):
            continue
        else:
            line = line.split('\t')
            if str(line[2]) == 'chrI':
                g = int(line[3])
                if int(line[3]) in sites1:
                    c = int(c + 1)
                else:
                    d = int(d + 1)
            elif line[2] == 'chrII':
                g = int(line[3])
                if g in sites2:
                    c = int(c + 1)
                else:
                    d = int(d + 1)
            elif line[2] == 'chrIII':
                g = int(line[3])
                if g in sites3:
                    c = int(c + 1)
                else:
                    d = int(d + 1)
            elif line[2] == 'chrIV':
                g = int(line[3])
                if g in sites4:
                    c = int(c + 1)
                else:
                    d = int(d + 1)
            elif line[2] == 'chrV':
                g = int(line[3])
                if g in sites5:
                    c = int(c + 1)
                else:
                    d = int(d + 1)
            elif line[2] == 'chrX':
                g = int(line[3])
                if g in sitesX:
                    c = int(c + 1)
                else:
                    d = int(d + 1)
            else:
                continue

#generate count data for variables e and f defined earlier using nucleosome start SAM file as input
with open(sys.argv[3], 'rt') as x:
    for line in x:
        if line[0].startswith('@'):
            continue
        else:
            line = line.split('\t')
            if line[2] == 'chrI':
                g = int(line[3])
                if g in sites1:
                    e = int(e + 1)
                else:
                    f = int(f + 1)
            elif line[2] == 'chrII':
                g = int(line[3])
                if g in sites2:
                    e = int(e + 1)
                else:
                    f = int(f + 1)
            elif line[2] == 'chrIII':
                g = int(line[3])
                if g in sites3:
                    e = int(e + 1)
                else:
                    f = int(f + 1)
            elif line[2] == 'chrIV':
                g = int(line[3])
                if g in sites4:
                    e = int(e + 1)
                else:
                    f = int(f + 1)
            elif line[2] == 'chrV':
                g = int(line[3])
                if g in sites5:
                    e = int(e + 1)
                else:
                    f = int(f + 1)
            elif line[2] == 'chrX':
                g = int(line[3])
                if g in sitesX:
                    e = int(e + 1)
                else:
                    f = int(f + 1)
            else:
                continue

file.write('\t'+str('SampleA')+'\t'+str('SampleB')+'\n'+str('# reads at defined position')+'\t'+str(c)+'\t'+str(e)+'\n'+str('# remaining reads')+'\t'+str(d)+'\t'+str(f))

file.close()
