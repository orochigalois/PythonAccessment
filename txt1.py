import os
finalfile = open('final.txt', 'w')
for root, dirs, files in os.walk("."):
	for file in files:
		tempfile = open(file)
		finalfile.write('++++++++++'+file+'++++++++++\n\n\n\n'+tempfile.read() + '\n\n\n\n')
		tempfile.close()
finalfile.close()