import csv
sales = (
    ("Peter", (78, 70, 65)),
    ("John", (88, 80, 85)),
    ("Tony", (90, 99, 95)),
    ("Henry", (80, 70, 55)),
    ("Mike", (95, 90, 95)),
)
with open('./monitor.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'Jan', 'Feb', 'Mar'])
    for name, qa in sales:
        writer.writerow([name, qa[0], qa[1], qa[2]])
