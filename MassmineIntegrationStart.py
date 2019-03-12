import subprocess
import json

# Commands can probably be passed in with an array
args = ["-t twitter-search","-c 1","-q \"bugcrowd\""]
command = "massmine"
for a in args:
	command+=" "+a
process = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
output, error = process.communicate()

# The output can be output to the screen
print output

# Or it can be saved to a file for parsing later
with open("outputFile.txt","w") as f:
	if error == None:
		for x in output:
			f.write(x)
