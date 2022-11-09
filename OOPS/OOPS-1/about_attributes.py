class Expense_Tracker:
    # class attribues
    Expense_Tracker_version = 0.1

    def __init__(self, tracker_category, opening_balance, budget):
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget


home_tracker = Expense_Tracker('home', 3000, 10000)
shopping_tracker = Expense_Tracker('shopping', 4000, 20000)

print(home_tracker.tracker_category)
print(shopping_tracker.tracker_category)

print(home_tracker.__dict__)
print(shopping_tracker.__dict__)

print(getattr(home_tracker, 'budget'))
# print(getattr(shopping_tracker, 'bud')) - error

print(hasattr(home_tracker, 'open'))
# checks whether the attribute exists or not

delattr(home_tracker, 'budget')
print(home_tracker.__dict__)
