from .add_employee import add_employee
from .view_employees import view_employees
from .search_employee import search_employee
from .update_employee import update_employee
from .delete_employee import delete_employee
#The . before each module name means “import from the same package” (the employee_system folder).

def menu():
    while True:
        print("===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        print()

if __name__ == "__main__":
    menu()
