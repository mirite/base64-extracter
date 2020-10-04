import re
import base64
from webptools import dwebp
import os

text=""

with open("sample.html","r") as f:
	text=f.read()

if not os.path.exists('output'):
    os.makedirs('output')

if not os.path.exists('output/assets'):
    os.makedirs('output/assets')

if not os.path.exists('output/tmp'):
    os.makedirs('output/tmp')
	
print("File is " + str(len(text)) + " characters")

objects=re.findall(r'(data:[a-z]+\/[a-z\+]+;base64,)([a-zA-Z0-9\!\$\&\'\,\*\+\,\;\=\-\.\_\~\:\@\/\?\%]*)[\s\)\"]+', text)

print("Found " + str(len(objects)) + " encoded objects")

x=0
for f in objects:
	x=x+1

	print("Writing dat file for file " + str(x))
	with open("output/tmp/file" + str(x) + ".dat","w") as newFile:
		newFile.write(f[0] + f[1])
	
	if("webp" in f[0]):
		type="webp"
	elif("png" in f[0]):
		type="png"
	elif("svg" in f[0]):
		type="svg"

	if type != "":

		finalPath="assets/image" + str(x) + "." + type
		path="output/" + finalPath

		print("Known file type. Writing " + path)

		if type=="webp":
			path="output/tmp/" + str(x) + ".webp"
			with open(path,"wb") as newFile:
				encodedString=f[1].encode()
				newFile.write(base64.decodebytes(encodedString))

			finalPath="assets/image" + str(x) + ".png"
			dwebp(path,"output/assets/image" + str(x) + ".png","-o")

		else:
			with open(path,"wb") as newFile:
				encodedString=f[1].encode()
				newFile.write(base64.decodebytes(encodedString))

		text=text.replace(f[0]+f[1],finalPath)

with open("output/output.html","w") as newFile:
	newFile.write(text)