from .data_model import employees, MAX_EMPLOYEES
from .helpers import find_by_id, next_id, has_capacity

def add_employee():
    if not has_capacity(MAX_EMPLOYEES):
        print(f"Cannot add new employee: maximum of {MAX_EMPLOYEES} reached.")
        return None

    id_input = input("Enter ID (leave blank to auto-generate): ").strip()
    if id_input == "":
        emp_id = next_id()
    else:
        try:
            emp_id = int(id_input)
        except ValueError:
            print("Invalid ID. Must be an integer.")
            return None
        if find_by_id(emp_id) is not None:
            print(f"An employee with ID {emp_id} already exists.")
            return None

    name = input("Enter name: ").strip()
    department = input("Enter department: ").strip()
    role = input("Enter role: ").strip()
    salary_input = input("Enter salary: ").strip()
    try:
        salary = float(salary_input)
    except ValueError:
        print("Invalid salary. Must be a number.")
        return None

    new_emp = {"id": emp_id, "name": name, "department": department, "role": role, "salary": salary}
    employees.append(new_emp)
    print(f"\nEmployee added with ID {emp_id}.\n")
    return new_emp

