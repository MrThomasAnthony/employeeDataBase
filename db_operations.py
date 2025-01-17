import os

def load_data(filename="employees.txt"):
    #Load the database file into a list
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_data(data, filename="employees.txt"):
    #Save the data list back to the database file
    with open(filename, "w") as file:
        file.writelines(f"{line}\n" for line in data)

def check_id(employee_id, data):
    #Check if an employee ID exists in the data
    return any(line.startswith(f"{employee_id}:") for line in data)

def add_employee(employee_id, first_name, last_name, department, data):
    #Add a new employee to the database
    data.append(f"{employee_id}:{first_name}:{last_name}:{department}")
    return data

def remove_employee(employee_id, data):
    #Remove an employee by ID
    return [line for line in data if not line.startswith(f"{employee_id}:")]

def search_employee(employee_id, data):
    #Search for an employee by ID
    for line in data:
        if line.startswith(f"{employee_id}:"):
            return line.split(":")
    return None
