from urllib.request import urlopen

link = "http://flepeint.ccfaculty.org/java143/hw7/hamlet.text"

openfile = urlopen(link)
myfile = openfile.read()
myfile(type)