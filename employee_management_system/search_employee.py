from .data_model import employees
from .helpers import find_by_id, find_by_name, print_table

def search_employee():
    choice = input("Search by (1) ID or (2) Name? Enter 1 or 2: ").strip()
    if choice == "1":
        id_input = input("Enter ID: ").strip()
        try:
            emp_id = int(id_input)
        except ValueError:
            print("Invalid ID.")
            return None
        emp = find_by_id(emp_id)
        if emp:
            print_table([emp])
            return [emp]
        else:
            print("Employee not found.")
            return []
    elif choice == "2":
        name = input("Enter name (or part of name): ").strip()
        matches = find_by_name(name)
        if matches:
            print_table(matches)
        else:
            print("Employee not found.")
        return matches
    else:
        print("Invalid choice.")
        return None


