from .data_model import employees
from .helpers import print_table

def view_employees():
    print_table(employees)
    return employees
