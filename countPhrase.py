import csv

phrase = "single malt scotch"
count = 0
with open('iowa-liquor-sample.csv', 'rb') as excelFile:
    reader = csv.reader(excelFile)
    for line in reader:
         present = 0
         for cell in line:
             if phrase in cell.lower():
                 present = 1
         if present == 1:
             count += 1

print("Number of Occurrences = " + str(count))
