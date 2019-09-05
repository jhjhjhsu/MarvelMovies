"""
MarvelMovies.py

sort marvel movies by gross amount

"""


import sys
import urllib.request


#import marvel movies data from github
url = "https://raw.githubusercontent.com/jhjhjhsu/MarvelMovies/master/Movie.txt"

try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print(error, file = sys.stderr)
    sys.exit(1)


for line in lines:   #line is a sequence of bytes.
    s = line.decode("utf-8") #Convert sequence of bytes to string of characters.
                     
    def score (s):
        fields = s.split(",")
        fields = int(fields)
        return fields[1]

    s.sort (key = score)
    print (s, end = "")
     

lines.close()


sys.exit(0)
