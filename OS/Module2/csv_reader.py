import csv

# Use 'with' to open the file, ensuring it gets closed properly
with open("csv_file.txt", mode='r', newline='') as f:
    csv_f = csv.reader(f)
    for row in csv_f:
        # Ensure that the row has the expected number of elements
        if len(row) == 3:
            name, phone, role = row
            print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
        else:
            print("Row does not contain exactly three elements:", row)


hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)


users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

