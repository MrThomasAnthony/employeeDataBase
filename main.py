import db_operations as db

def display_menu():
    #Display the main menu
    print("-------------------------------")
    print("\tEmployees:")
    print("-------------------------------")
    print("Select one of the following:")
    print("1) Add a new employee")
    print("2) Search for an employee")
    print("3) Remove an employee")
    print("4) Display employees")
    print("5) Exit")
    print("-------------------------------\n")

def main():
    #Main function to handle user interaction
    data = db.load_data()
    
    while True:
        display_menu()
        option = input("Enter Your Option: ")
        
        if option == '1':
            while True:
                employee_id = input("Enter Employee ID: ")
                if not employee_id.isdigit():
                    print("ID must be numeric!")
                    continue
                if db.check_id(employee_id, data):
                    print("Employee ID already exists!")
                else:
                    break
            first_name = input("Enter Employee Firstname: ").strip()
            last_name = input("Enter Employee Lastname: ").strip()
            department = input("Enter Employee Department: ").strip()
            data = db.add_employee(employee_id, first_name, last_name, department, data)
            print("\nEmployee Added!")
        
        elif option == '2':
            employee_id = input("Enter Employee ID: ")
            result = db.search_employee(employee_id, data)
            if result:
                print(f"\nID: {result[0]}, \nFirstname: {result[1]}, \nLastname: {result[2]}, \nDepartment: {result[3]}\n")
            else:
                print("\nEmployee Not Found!")
        
        elif option == '3':
            employee_id = input("Enter Employee ID: ")
            if not db.check_id(employee_id, data):
                print("\nEmployee Not Found!")
            else:
                data = db.remove_employee(employee_id, data)
                print("\nEmployee Deleted!")
        
        elif option == '4':
            if not data:
                print("\nNo employees in the database.")
            else:
                print("\nEmployee Database:")
                for line in data:
                    fields = line.split(":")
                    print(f"ID: {fields[0]}, Firstname: {fields[1]}, Lastname: {fields[2]}, Department: {fields[3]}")
        
        elif option == '5':
            db.save_data(data)
            print("\nGoodbye!")
            break
        
        else:
            print("\nInvalid option. Try again!")

main()
