from .data_model import employees
from .helpers import find_by_id

def delete_employee():
    id_input = input("Enter employee ID to delete: ").strip()
    try:
        emp_id = int(id_input)
    except ValueError:
        print("Invalid ID.")
        return False

    emp = find_by_id(emp_id)
    if not emp:
        print("Employee not found.")
        return False

    confirm = input(f"Are you sure you want to delete {emp['name']} (ID {emp_id})? (y/N): ").strip().lower()
    if confirm == 'y':
        employees.remove(emp)
        print("Employee deleted.")
        return True
    else:
        print("Deletion cancelled.")
        return False

