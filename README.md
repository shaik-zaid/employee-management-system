# 🧑‍💼 Employee Management System (Python Functions Only)

A simple, menu-driven **Employee Management System** built using **Python functions only** — no OOP, no database, and no file handling.  
This project is designed for beginners to understand how to structure modular Python applications using **lists, dictionaries, loops, and conditionals**.

---

## 📋 Features

✅ **Add Employee** – Add a new employee with ID, Name, Department, Role, and Salary.  
✅ **View Employees** – Display all employee records in a clean table format.  
✅ **Search Employee** – Search by Employee ID or Name.  
✅ **Update Employee** – Update Department, Role, or Salary of an existing employee.  
✅ **Delete Employee** – Remove an employee record by ID.  
✅ **Exit Program** – Safely end the program.  

---

## 🗂️ Project Structure

```
employee-management-system/
│
├── data_model.py          # Stores employee list and constants
├── helpers.py             # Reusable utility functions (find_by_id, print_table, etc.)
│
├── add_employee.py        # Add a new employee (interactive)
├── view_employees.py      # Display all employees
├── search_employee.py     # Find employee by ID or name
├── update_employee.py     # Edit existing employee details
├── delete_employee.py     # Remove an employee record
│
└── main.py                # Main menu (entry point)
```

---

## 💾 Data Model

Employees are stored in a **list of dictionaries** (in-memory data, no files).

```python
employees = [
    {"id": 1, "name": "Alice", "department": "HR", "role": "Manager", "salary": 50000},
    {"id": 2, "name": "Bob", "department": "IT", "role": "Developer", "salary": 60000}
]
```

Each employee record contains:
- `id` – Unique employee ID  
- `name` – Full name of the employee  
- `department` – Department name  
- `role` – Job title  
- `salary` – Employee’s monthly salary  

---

## ⚙️ Functional Overview

| Function | Description |
|-----------|--------------|
| `add_employee()` | Add a new employee (with validation and ID check) |
| `view_employees()` | Display all employees in a formatted table |
| `search_employee()` | Find employee by ID or name |
| `update_employee()` | Update department, role, or salary |
| `delete_employee()` | Remove employee from the list |
| `menu()` | Display main menu and handle user input |

---

## 🧠 Requirements

- Python **3.8+**
- Basic understanding of:
  - Lists and Dictionaries  
  - Functions  
  - Loops & Conditionals  
  - Input/Output operations

---

## ▶️ How to Run

1. **Clone or Download** this repository  
   ```bash
   git clone https://github.com/shaik-zaid/employee-management-system.git
   cd employee-management-system
   ```

2. **Run the main file**
   ```bash
   python -m employee_management_system.main
   ```
   or
   ```bash
   python main.py
   ```

3. **Follow the menu prompts**

```
===== Employee Management System =====
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit
Enter your choice:
```

---

## 🧩 Example Usage

**Adding an Employee:**
```
Enter ID (leave blank to auto-generate): 1
Enter name: Alice
Enter department: HR
Enter role: Manager
Enter salary: 50000

Employee added with ID 1.
```

**Viewing Employees:**
```
ID   Name                      Department      Role              Salary
-----------------------------------------------------------------------
1    Alice                     HR              Manager              50000.00
```

---

## 🧹 Exit Option
Choose **6** from the menu to exit the program:
```
Exiting Employee Management System. Goodbye!
```

---

## 🧩 Learning Goals

This project helps you learn:
- Function-based programming structure
- Modular code organization
- Reusability with helper functions
- Input validation and user interaction
- Console-based CRUD operations

---

## 📁 Recommended Next Steps

After mastering this, you can enhance the project by:
- Adding **file storage (JSON/CSV)** to save data permanently  
- Using **classes (OOP)** for scalability  
- Creating a **Tkinter GUI** version  
- Adding **unit testing** for automation

---

## 👨‍💻 Author

**Shaik Zaid**  
📧 [shaikzaid9393@gmail.com]  
💼 [LinkedIn Profile](https://www.linkedin.com/in/shaik-zaid-832407331/)  
🐙 [GitHub](https://github.com/shaik-zaid)

---

⭐ **If you find this project helpful, please star the repository!**
