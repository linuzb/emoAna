import csv

with open("Train/Train_DataSet.csv") as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    i = 0
    for row in f_csv:
        print(row[2])
        if i == 5:
            break
        else:
            i += 1
    
