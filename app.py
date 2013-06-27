import urllib2
import csv
from BeautifulSoup import BeautifulSoup
f = open('list','w')
with open('list.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        for cell in row:
            try:
                soup = BeautifulSoup(urllib2.urlopen(cell))
                print soup.title.string
                f.write(cell+',\n')
            except:
                print 'ERR : ',cell,' couldn\'t be parsed!'
                f.write(cell+',\n')
