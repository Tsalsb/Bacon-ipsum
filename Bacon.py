

import urllib
import json

url = "https://baconipsum.com/api/?type=meat-and-filler"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data

for i in data:
	print i + "\n\n"
