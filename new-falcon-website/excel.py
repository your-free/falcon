#!/usr/bin/python
import csv, json
csvreader = csv.reader(open('tube.xls', 'rb')
data = []
for row in csvreader:
    r = []
    for field in row:
        if field == '': field = None
        else: field = unicode(field, 'ISO-8859-1')
        r.append(field)
    data.append(r)
jsonStruct = {
    'header': data[0],
    'data': data[1:]
}
open('data.json', 'wb').write(json.dumps(jsonStruct))