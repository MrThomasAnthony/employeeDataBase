## Employee Database Management System

## Overview
This Python program is designed to manage an employee database stored in a text file (`employees.txt`). The program provides functionalities to:
- Add new employees.
- Search for existing employees.
- Remove employees.
- Display all employees.

The program uses a menu-driven interface, allowing users to interact with the database efficiently.

---

## Features
1. **Add Employee**:
   - Prompts the user to enter an employee's ID, first name, last name, and department.
   - Ensures the employee ID is unique.
   - Appends the new employee's details to the database file.

2. **Search Employee**:
   - Allows the user to search for an employee by their ID.
   - Displays the employee's details if found; otherwise, notifies the user that the employee does not exist.

3. **Remove Employee**:
   - Prompts the user for an employee ID to delete.
   - If the employee exists, they are removed from the database.
   - Displays a confirmation message upon successful removal.

4. **Display Employees**:
   - Outputs a clean and formatted list of all employees in the database.
   - Notifies the user if the database is empty.

5. **Exit**:
   - Saves any changes made to the database and exits the program.

---

## File Structure
- **`db_operations.py`**:
  - Contains functions for core database operations, such as loading, saving, adding, searching, and removing employees.
- **`main.py`**:
  - Handles user interaction through a menu-driven interface.

---

## Database File Format
The employee database is stored in a text file named `employees.txt`. Each employee record is represented by a single line with fields separated by colons (`:`):

```
<employee_id>:<first_name>:<last_name>:<department>
```

### Example:
```
1234:John:Doe:Science
4321:Jane:Smith:Arts
9991:Matt:Davis:Math
```

---

## How to Run the Program
1. Ensure you have Python 3 installed on your system.
2. Place the `db_operations.py` and `main.py` files in the same directory.
3. Create an `employees.txt` file in the same directory if it does not already exist.
4. Open a terminal or command prompt and navigate to the directory containing the files.
5. Run the program using the command:

   ```
   python main.py
   ```

---

## Input Validation
- Employee IDs must be numeric and unique.
- Fields such as first name, last name, and department cannot be empty.
- Invalid menu options are flagged, and users are prompted to try again.

---

## Error Handling
- If the `employees.txt` file is missing, the program will create it automatically when adding a new employee.
- Handles file read/write errors gracefully.
- Prevents invalid or malformed inputs.

---

## Dependencies
This program uses only the Python Standard Library and requires no additional installations.

---

## Future Enhancements
- Add functionality to sort employees by ID, name, or department.
- Implement a graphical user interface (GUI).
- Allow export of the employee database to formats like CSV or Excel.
