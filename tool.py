import re
import base64

text=""

with open("sample.html","r") as f:
	text=f.read()

print("File is " + str(len(text)) + " characters")

objects=re.findall(r'(data:[a-z]+\/[a-z\+]+;base64,)([a-zA-Z0-9\!\$\&\'\,\*\+\,\;\=\-\.\_\~\:\@\/\?\%]*)[\s\)\"]+', text)

print("Found " + str(len(objects)) + " encoded objects")

x=0
for f in objects:
	x=x+1

	print("Writing dat file for file " + str(x))
	with open("output/file" + str(x) + ".dat","w") as newFile:
		newFile.write(f[0] + f[1])
	
	if("webp" in f[0]):
		type="webp"
	elif("png" in f[0]):
		type="png"
	elif("svg" in f[0]):
		type="svg"

	if type != "":

		path="output/image" + str(x) + "." + type
		print("Known file type. Writing " + path)

		with open(path,"wb") as newFile:
			encodedString=f[1].encode()
			newFile.write(base64.decodebytes(encodedString))