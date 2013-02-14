#!/usr/bin/python

import csv,json,sys,codecs

try:
    json_data = json.load(open(sys.argv[1]))
except:
    print "Error"
    exit(1)

csv_file = codecs.open('output.csv','w','utf-8')
csv_output = csv.writer(csv_file)

if len(json_data[0]) == 1 and type(json_data[0][json_data[0].keys()[0]]) == dict:
    item = json_data[0].keys()[0]
    csv_output.writerow(json_data[0][item].keys())
    for thing in json_data:
        try:
            csv_output.writerow([str(i).decode('ascii') for i in thing[item].values()])
        except:
            print thing[item]
else:
    csv_output.writerow(json_data[0].keys())
    for thing in json_data:
        try:
            csv_output.writerow(thing.values())
        except:
            print thing
csv_file.close()
