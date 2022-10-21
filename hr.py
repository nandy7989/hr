
"""fields = {'employee_name': {'prompt': 'Enter name: ', 'value': None}
          'ssn': {'prompt': ' enter soc sec: ', 'value': None}}
for ...
fields['name']['value'] = input(fields['name']['prompt'])
print(fields)"""

def validate_employeename(employee_name):
    if not (5 <= len(employee_name) <= 20):
        return False
    return True

def adding_multipleemployees():
    employee = {
        'employee_name': {'prompt': 'Enter employee name: ', 'value': None, 'validation_func': validate_employeename},
        'employee_phone': {'prompt': 'Enter employee phone: ', 'value': None, },
        'employee_address': {'prompt': 'Enter employee add: ', 'value': None},
        'employee_ssn': {'prompt': 'Enter employee ssn: ', 'value': None},
        'employee_dob': {'prompt': 'Enter employee dob: ', 'value': None},
    }
    for field_name,meta_data in employee.items():
        meta_data['value'] = input(meta_data['prompt'])
    z
    print(employee)

    """while True:
        employee_name = input("Enter Employee name , 99 to quit")
        if employee_name == "99":
            break
        employee_address = input("Enter Employee address")
        employee_ssn = input("Enter Employee SSN")
        employee_dob = input("Enter Employee DOB")
        employee_jobtitle = input("Enter Employee job title")
        employee_startdate = input("Enter Employee start date")
        employee_enddate = input("Enter Employee end date")
        employees.append([
            employee_name,
            employee_address,
            employee_ssn,
            employee_dob,
            employee_jobtitle,
            employee_startdate,
            employee_enddate
        ])
    print(employees)
    exit(1)
    return employees"""
adding_multipleemployees()

def validate_dob(employee_dob):
    dob = employee_dob.split("/")
    mm = int(dob[0])
    dd = int(dob[1])
    yyyy = int(dob[2])
    if not (1 <= mm <= 12):
        return False
    else:
        if mm in (1, 3, 5, 7, 8, 10, 12) and not (1 <= dd <= 31):
            return False
        elif mm in (4, 6, 9, 11) and not (1 <= dd <= 30):
            return False
        elif mm == 2 and not (1 <= dd <= 27):
            return False
    return True



def validate_employeessn(employee_ssn):
    if len(employee_ssn) == 11:
        if employee_ssn[3] + employee_ssn[6] == "--":  # 999-99-9999
            if employee_ssn.replace("-", "").isdigit():
                return True
            else:
                return False
        else:
            return False
    else:
        return False
