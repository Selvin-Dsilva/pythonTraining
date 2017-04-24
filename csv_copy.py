import csv

with open('FL_sample.csv') as csv_data, open ("output.csv",mode='w') as op_csv:
    read_csv = csv.reader(csv_data)
    write_csv=csv.writer(op_csv)
    header =next(read_csv)
    even_head=[]
    for i in range(0,len(header)):
        if i%2==0:
            even_head.append(header[i])
        if len(even_head)==6:
            break
    write_csv.writerow(even_head)
    for data in read_csv:
        op_csv.write(','.join((data[0],data[2],data[4],data[6],data[8],data[10],'\n')))

