import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    
    with open(csv_file_location) as f:  # Use 'with' for file handling
        employee_file = csv.DictReader(f, dialect='empDialect')
        
        employee_list = []

        for data in employee_file:
            employee_list.append(dict(data))

    return employee_list

# Use raw string for the file path
employee_list = read_employees(r'C:\Users\laney\python_projects\Class\OS\Module2\employee_file.csv')

print(employee_list)