class Expense_Tracker:
    # class attribue
    Expense_Tracker_version = 0.1

    def __init__(self, tracker_category, opening_balance, budget):
        # instant/object attributes
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget

    # instance method
    def get_opening_balance(self):
        return self.opening_balance

    # instance method
    def check_balance(self, limit=1000):
        if self.budget >= limit:
            return True
        else:
            return "your budget is lesser than limit"

    @staticmethod
    def convert_amount(amount):
        return float(amount)

    # Factory method
    @classmethod
    def get_attriubtes_from_string(cls, diary_entry: str):
        tracking_category, opening_balance, budget = diary_entry.split(" ")

        return Expense_Tracker(tracking_category.capitalize(),
                               cls.convert_amount(opening_balance),
                               cls.convert_amount(budget))


home_tracker = Expense_Tracker('home', 3000, 10000)
shopping_tracker = Expense_Tracker('shopping', 4000, 20000)

print(home_tracker.get_opening_balance())
print(shopping_tracker.get_opening_balance())
print(Expense_Tracker.get_opening_balance(home_tracker))

print(shopping_tracker.check_balance())
print(home_tracker.check_balance(2000000))

print(home_tracker.convert_amount(1000))

buisness_tracker = Expense_Tracker.get_attriubtes_from_string(
    "business 5000 1000")
print(buisness_tracker.__dict__)
