#将目录下所有文件的编码 从gb18030转换为utf8
#用法:
#python coding1.py
#What's your InputPath?D:\input
#What's your OutputPath?D:\output


import os

inputPath = raw_input("What's your InputPath?")
outputPath = raw_input("What's your OutputPath?")
for root, dirs, files in os.walk(inputPath):
    for file in files:
        inputFile  = open(os.path.join(inputPath, file))
        outputFile = open(os.path.join(outputPath, file),'w')
        tempString = inputFile.read()
        tempString = tempString.decode('gb18030')
        tempString = tempString.encode('utf-8')
        outputFile.write(tempString)
        inputFile.close()
        outputFile.close()