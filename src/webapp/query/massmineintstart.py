import subprocess
import json
import os

# Commands can probably be passed in with an array

os.system("massmine --task=twitter-search --query=love --count=100 --output=mydata.csv")



#"massmine --task=twitter-search --query=love --count=100 | jsan --output=mydata.csv"