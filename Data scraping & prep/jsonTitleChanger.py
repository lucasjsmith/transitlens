__author__ = 'lucas'

from os import path

daytime = 'sun9PM'

with open('geodata/{}.js'.format(daytime), 'r' ) as infile:
    outString = ''
    for line in infile:
        outString = outString + line
    for index in range(0,290):
        outString = outString.replace('\"' + str(index) + '\"', '\"i' + str(index) + '\"')

    outString = outString.replace('.000000','')

    newfile = open('geodata/{}-i.js'.format(daytime), 'w')
    newfile.write(outString)
    newfile.close()



#     /Users/lucas/Dropbox/College/IML thesis/PyCharm/TrimetAPI/TrimetAPI/production data/5-1-2015_3:00%20PM/durations-3.csv
# /Users/lucas/Dropbox/College/IML thesis/storm mirror/transitlens/geodata/wkday3PM.js