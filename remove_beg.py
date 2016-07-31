import csv
pinfocsv = 'pact2.csv'
with open(pinfocsv, 'rb') as f:
    reader = csv.reader(f,  delimiter='|')
    name_list = None
    values = []
    for row in reader:
        if name_list == None:
            name_list = row
            print name_list
        else:
            values.append(row)
    f.close()
with open(pinfocsv, 'w') as f:
    f.write( '|'.join(name_list[1:])+'\n')
    for row in values:
    	f.write('|'.join(row[1:])+'\n')
    f.close()
