import os
inputFile = open('D:\\1.txt', 'r')
finalfile=open('D:\\2.txt', 'w')
for line in inputFile:
    finalfile.write(line.strip())
inputFile.close()
finalfile.close()