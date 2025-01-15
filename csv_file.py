import csv
with open("AI_microdegree.csv",mode="w",newline='') as csvfile:
    add=csv.writer(csvfile)
    add.writerow(['Name','Address','Trade'])
    add.writerow(['Fareesa','Hyd','AIPA'])
    add.writerow(['Hibah','Telangana','AIPA'])
    print("CSV created successfully!")

with open("AI_microdegree.csv",newline='') as csvfile:
    csv1=csv.reader(csvfile)
    for row in csv1: 
        print(row)