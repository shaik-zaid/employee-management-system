# Simple utility functions for the employee system 
#data_model have list of employees and MAX_EMPLOYEES 


from .data_model import employees

def find_by_id(emp_id):
    """Return the employee dict with the given id, or None if not found."""
    for i in employees:
        if i.get("id") == emp_id:
            return i
    return None

def find_by_name(name):
    """Return a list of employees matching the name substring (case-insensitive)."""
    name = name.strip().lower()
    return [e for e in employees if name in e.get("name", "").lower()]

def next_id():
    """Generate the next id (1-based) not already used. Simple increment."""
    if not employees:
        return 1
    return max(e["id"] for e in employees) + 1

def has_capacity(max_employees):
    """Return True if we can add more employees."""
    return len(employees) < max_employees

def print_table(rows):
    """Print a neat table of employees. Handles empty list.
       It expects one input: rows, which should be a list of employee dictionaries."""
    if not rows:
        print("\nNo employees found.\n")
        return

    header = f"{'ID':<4} {'Name':<25} {'Department':<15} {'Role':<15} {'Salary':>10}"
    # :<4 Left-align text in 4 spaces
    print("\n" + header)
    print("-" * len(header))
    for e in rows:
        print(f"{e['id']:<4} {e['name']:<25} {e['department']:<15} {e['role']:<15} {e['salary']:10.2f}")
    print()
