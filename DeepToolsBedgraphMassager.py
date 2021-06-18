import sys

#this program takes bedgraph output from the DeepTools bamCoverage program and separates out bins lumped together (because of adjacency and identical coverage)
#into base pair resolution
x = open(sys.argv[1], 'r')
output = str(sys.argv[2])
f = open(output, 'w')

def splitter():
    list=line.split()
    a=str(list[0])
    b=int(list[1])
    c=int(list[2])
    d=float(list[3])
    e=int(c-b)
    g=int(b+1)
    while e >= 1:
        f.write(str(a)+'\t'+str(b)+'\t'+str(g)+'\t'+str(d)+'\n')
        b = b+1
        e = e-1
        g = g+1
        if e == 0:
            break

for line in x:
    list = line.split()
    if str(list[3]) == '0':
        continue
    elif int(list[2])- int(list[1])==1:
        f.write(line)
    else:
        splitter()

f.close()
