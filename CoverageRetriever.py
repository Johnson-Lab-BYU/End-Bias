import sys
import threading

#This program is designed to output average coverage ratio data at a single bp resolution at a
#user-defined distance from known fragment ends.  The input for this program is output from binMassager.py.
#The output of this program is a single value, necessitating multiple program calls with parameter changes.

z = int(sys.argv[3]) #distance from cutsite
output = str(sys.argv[4]) #name of output
f = open(output, 'w')

sites1 = [] #empty lists to be filled with cutsites by chromosome, argument 1
sites2 = []
sites3 = []
sites4 = []
sites5 = []
sitesX = []
coverage1 = {} #empty dictionaries to be filled with bamCompare data, argument 2
coverage2 = {}
coverage3 = {}
coverage4 = {}
coverage5 = {}
coverageX = {}
prime1 = [] #locations upstream or downstream of cutsite file using variable z, argument 3
prime2 = []
prime3 = []
prime4 = []
prime5 = []
primeX = []
data1 = [] #coverage values based on distance from cutsite
data2 = []
data3 = []
data4 = []
data5 = []
dataX = []

#separate cutsite file into lists of each chromosome
with open(sys.argv[1], 'rt') as x:
    for line in x:
        if line.startswith('chr1') or line.startswith('chrI'):
            sites1.append(line)
        elif line.startswith('chr2') or line.startswith('chrII'):
            sites2.append(line)
        elif line.startswith('chr3') or line.startswith('chrIII'):
            sites3.append(line)
        elif line.startswith('chr4') or line.startswith('chrIV'):
            sites4.append(line)
        elif line.startswith('chr5') or line.startswith('chrV'):
            sites5.append(line)
        elif line.startswith('chrX'):
            sitesX.append(line)
        else:
            continue

#separate bamCompare file into dictionaries of each chromosome
with open(sys.argv[2], 'rt') as y:
    for line in y:
        if line.startswith('chr1') or line.startswith('chrI'):
            line = line.split()
            coverage1[line[2]] = line[3]
        elif line.startswith('chr2') or line.startswith('chrII'):
            line = line.split()
            coverage2[line[2]] = line[3]
        elif line.startswith('chr3') or line.startswith('chrIII'):
            line = line.split()
            coverage3[line[2]] = line[3]
        elif line.startswith('chr4') or line.startswith('chrIV'):
            line = line.split()
            coverage4[line[2]] = line[3]
        elif line.startswith('chr5') or line.startswith('chrV'):
            line = line.split()
            coverage5[line[2]] = line[3]
        elif line.startswith('chrX'):
            line = line.split()
            coverageX[line[2]] = line[3]
        else:
            continue

#create function that uses location in cutsite list to use as a key to call the corresponding location in the bamCompare dictionary and return the associated value
#each thread represents one chromosome
def thread1():
    for index in sites1:
        element = index.split()
        threePrime = int(element[2])-int(z)
        fivePrime = int(element[1])+int(z)
        prime1.append(fivePrime)
        prime1.append(threePrime)
    for index in prime1:
        for key,value in coverage1.items():
            if str(index) == str(key):
                data1.append(float(value))
            else:
                continue

def thread2():
    for index in sites2:
        element = index.split()
        threePrime = int(element[2])-int(z)
        fivePrime = int(element[1])+int(z)
        prime2.append(fivePrime)
        prime2.append(threePrime)
    for index in prime2:
        for key,value in coverage2.items():
            if str(index) == str(key):
                data2.append(float(value))
            else:
                continue

def thread3():
    for index in sites3:
        element = index.split()
        threePrime = int(element[2])-int(z)
        fivePrime = int(element[1])+int(z)
        prime3.append(fivePrime)
        prime3.append(threePrime)
    for index in prime3:
        for key,value in coverage3.items():
            if str(index) == str(key):
                data3.append(float(value))
            else:
                continue

def thread4():
    for index in sites4:
        element = index.split()
        threePrime = int(element[2])-int(z)
        fivePrime = int(element[1])+int(z)
        prime4.append(fivePrime)
        prime4.append(threePrime)
    for index in prime4:
        for key,value in coverage4.items():
            if str(index) == str(key):
                data4.append(float(value))
            else:
                continue

def thread5():
    for index in sites5:
        element = index.split()
        threePrime = int(element[2])-int(z)
        fivePrime = int(element[1])+int(z)
        prime5.append(fivePrime)
        prime5.append(threePrime)
    for index in prime5:
        for key,value in coverage5.items():
            if str(index) == str(key):
                data5.append(float(value))
            else:
                continue

def thread6():
    for index in sitesX:
        element = index.split()
        threePrime = int(element[2])-int(z)
        fivePrime = int(element[1])+int(z)
        primeX.append(fivePrime)
        primeX.append(threePrime)
    for index in primeX:
        for key,value in coverageX.items():
            if str(index) == str(key):
                dataX.append(float(value))
            else:
                continue

#call each thread and then make sure each thread is done before continuing
if 0 == 0:
    t1=threading.Thread(target=thread1)
    t2=threading.Thread(target=thread2)
    t3=threading.Thread(target=thread3)
    t4=threading.Thread(target=thread4)
    t5=threading.Thread(target=thread5)
    t6=threading.Thread(target=thread6)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

#massage format for final output to be easy to read
final = data1 + data2 + data3 + data4 + data5 + dataX
ave = sum(final)/len(final)
f.write(str(ave))

f.close()
