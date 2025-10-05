from .data_model import employees
from .helpers import find_by_id

def update_employee():
    id_input = input("Enter employee ID to update: ").strip()
    try:
        emp_id = int(id_input)
    except ValueError:
        print("Invalid ID.")
        return False

    emp = find_by_id(emp_id)
    if not emp:
        print(f"No employee found with ID {emp_id}.")
        return False

    print("Leave field blank to keep current value.")
    new_dept = input(f"Department [{emp['department']}]: ").strip()
    new_role = input(f"Role [{emp['role']}]: ").strip()
    new_salary = input(f"Salary [{emp['salary']}]: ").strip()

    if new_dept:
        emp['department'] = new_dept
    if new_role:
        emp['role'] = new_role
    if new_salary:
        try:
            emp['salary'] = float(new_salary)
        except ValueError:
            print("Invalid salary input. Salary not changed.")
    print("Employee updated.\n")
    return True


