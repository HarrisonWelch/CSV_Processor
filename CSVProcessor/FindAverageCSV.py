import csv
import itertools
import __future__

with open("SerialRead2.csv", "r") as valuesFile:
    valuesFileReader = csv.reader(valuesFile)
    valuesList = []
    for row in valuesFileReader:
        if len (row) != 0:
            valuesList.append(row)




valuesFile.close()

#data = [eval(valuesList[0][0]) for row in valuesList]

#data = [map(float, valuesList[0][0]) for row in valuesList]

data = []

pressLst = []
celLst = []
fahLst = []
altLst = []

sumPrs = 0.00
sumCel = 0.00
sumFah = 0.00
sumAlt = 0.00

for x in range(0,(len(valuesList) - 1)):
    data.append(eval(compile(valuesList[x][1], '<string>', 'eval', __future__.division.compiler_flag)))
    data.append(eval(compile(valuesList[x][2], '<string>', 'eval', __future__.division.compiler_flag)))
    data.append(eval(compile(valuesList[x][3], '<string>', 'eval', __future__.division.compiler_flag)))
    data.append(eval(compile(valuesList[x][4], '<string>', 'eval', __future__.division.compiler_flag)))

print data
print len(data)
print len(valuesList)
for x in range(0,(len(valuesList) - 1)):
    sumPrs += data[(x * 4) + 0]
    sumCel += data[(x * 4) + 1]
    sumFah += data[(x * 4) + 2]
    sumAlt += data[(x * 4) + 3]
    print x
    print sumPrs
    
'''
    pressLst.append(eval(compile(valuesList[0][x][0][0][0], '<string>', 'eval', __future__.division.compiler_flag)))
      celLst.append(eval(compile(valuesList[0][0][x][0][0], '<string>', 'eval', __future__.division.compiler_flag)))
      fahLst.append(eval(compile(valuesList[0][0][0][x][0], '<string>', 'eval', __future__.division.compiler_flag)))
      altLst.append(eval(compile(valuesList[0][0][0][0][x], '<string>', 'eval', __future__.division.compiler_flag)))
''' 


total = 0.0

'''
out = open("SerialRead.csv", "r")
data = csv.reader(out)
data = [row for row in data]
out.close()

print data
print " "
print data[0]
print 
print type(data[0][0])

thing = eval(data[0][0])

print thing
print " "
print type(thing)
'''
#lst = valuesList[0].split(',')

#heartdis = heartdis[5:]

#values_flt = []

#values2 = list(itertools.chain.from_iterable(heartdis))

#for item in values2:
    #values_flt.append(float(item))

#print(values_flt)

print(type(valuesList[5]))

print(valuesList)
print(valuesList[0][0])

print type(valuesList[0][0])

print data
print type(data[1])

print ("The sum of all Pressures is " + str(sumPrs) + ".")
print ("The sum of all Celcius is " + str(sumCel) + ".")
print ("The sum of all Fahrenheit is " + str(sumFah) + ".")
print ("The sum of all Altitudes is " + str(sumAlt) + ".")

avgPrs = sumPrs / (len(valuesList) - 1)
avgCel = sumCel / (len(valuesList) - 1)
avgFah = sumFah / (len(valuesList) - 1)
avgAlt = sumAlt / (len(valuesList) - 1)

print ("The avgerage of all Pressures is " + str(avgPrs) + ".")
print ("The avgerage of all Celcius is " + str(avgCel) + ".")
print ("The avgerage of all Fahrenheit is " + str(avgFah) + ".")
print ("The avgerage of all Altitudes is " + str(avgAlt) + ".")

print len(valuesList)

'''
sumPrs = 0.00
sumCel = 0.00
sumFah = 0.00
sumAlt = 0.00

for x in range(len(data)):
    sumPress += pressLst[x]
    sumCel += celLst[x]
    sumFah += fahLst[x]
    sumAlt += altLst[x]
    
print sumPress
print sumCel
print sumFah
print sumAlt
'''
#print(i)


