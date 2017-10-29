import csv

def clean_csv(csv_file):
    lines = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            if len(row[0]) > 1:
                lines.append(row)
    print(len(lines))
    with open("PurchaseData.csv", "w") as f:
        writer = csv.writer(f, delimiter = ',')
        for line in lines:
            writer.writerow(line)

