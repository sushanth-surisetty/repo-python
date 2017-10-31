import csv
FN='mva11_demo.txt'
with open(FN,mode='r') as myCSVfl :
    data = csv.reader(myCSVfl)
    for row in data :
#..method1
        #print(row)
#..method2
        #for value in row :
        #    print(value)
#..method3
        #print(','.join(row))

## Hurray!!! output was printed successfully!
