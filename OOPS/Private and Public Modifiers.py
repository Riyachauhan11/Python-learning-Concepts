class Expense_Tracker:
    # class attribue
    Expense_Tracker_version = 0.1

    def __init__(self, tracker_category, opening_balance, budget):

        # instant/object attributes
        # Public attribute
        self.tracker_category = tracker_category

        # Private attributes
        self.__opening_balance = opening_balance
        self.__budget = budget

    # instance method
    # Private method
    def __get_opening_balance(self):
        return self.__opening_balance

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
print(home_tracker.tracker_category)
# print(home_tracker.opening_balance)
# print(home_tracker.__budget)
# print(home_tracker.__get_opening_balance)
'''all will throw an error of attribute being non existing'''

print(home_tracker.__dict__)
# accessing private attributes
print(home_tracker._Expense_Tracker__opening_balance)
print(home_tracker._Expense_Tracker__budget)

# accessing private method
print(home_tracker._Expense_Tracker__get_opening_balance())
