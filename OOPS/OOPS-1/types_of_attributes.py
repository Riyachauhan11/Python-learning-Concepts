class Expense_Tracker:
    # class attribue
    Expense_Tracker_version = 0.1

    def __init__(self, tracker_category, opening_balance, budget):
        # instant/object attributes
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget


home_tracker = Expense_Tracker('home', 3000, 10000)
shopping_tracker = Expense_Tracker('shopping', 4000, 20000)
print(home_tracker.__dict__)

print(home_tracker.Expense_Tracker_version)
print(shopping_tracker.Expense_Tracker_version)

home_tracker.Expense_Tracker_version = 0.2
print(home_tracker.Expense_Tracker_version)
print(shopping_tracker.Expense_Tracker_version)
