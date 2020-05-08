import xlrd
import csv
import os

def csv_from_excel(filename,directory):
    print(filename)
    wb = xlrd.open_workbook(directory+os.sep+filename)
    sh = wb.sheet_by_name(filename.replace(".xlsx",""))
    your_csv_file = open(filename.replace(".xlsx",".csv"), 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

directory="/Users/erans/PycharmProjects/metabolic_pathways/classifier/data/labeled_data/simulated-marathon/trainset/positive"
# runs the csv_from_excel function:
for filename in os.listdir(directory):
    csv_from_excel(filename,directory)