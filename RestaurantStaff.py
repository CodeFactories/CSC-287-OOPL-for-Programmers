# Staff Hierarchy at a Restaurant
# Parrent class Staff
class Staff:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    # Method to print staff member's name and ID
    def describe(self):
        print(f"Name: {self.name}, ID: {self.employee_id}")

    # Method perform_duties 
    def perform_duties(self):
        print("Performing general staff duties.")

# Subclass Chef
class Chef(Staff):
    def __init__(self, name, employee_id, specialty):
        # Initialize the parent class (Staff)
        super().__init__(name, employee_id)
        self.specialty = specialty

# Override method perform_duties
    def perform_duties(self):
        print(f"Cooking specialty dishes: {self.specialty}")

# Subclass: Waiter
class Waiter(Staff):
    def __init__(self, name, employee_id, tables_assigned):
        super().__init__(name, employee_id)
        self.tables_assigned = tables_assigned

    def perform_duties(self):
        print(f"Serving tables: {self.tables_assigned}.")

# Polymorphic Function
def staff_shift(staff_member):
    staff_member.describe()
    staff_member.perform_duties()

#____________main_________________
def main():
    # Generic staff member
    s = Staff("Alex Johnson", "S-001")
    # Chef
    c = Chef("Gordon Ramsay", "C-101", "Italian cuisine")
    # Waiter
    w = Waiter("Emily Clarke", "W-202", [1, 3, 5])

    # Test all staff members
    staff_shift(s)
    print()
    staff_shift(c)
    print()
    staff_shift(w)

if __name__ == "__main__":
    main()
