class Expense_Tracker:
    def __init__(self, date, description, transaction_type, amount):
        self.date = date
        self.description = description
        self.transaction_type = transaction_type
        self.amount = amount


obj1 = Expense_Tracker('12th Jan', 'dinner with friends', 'debit', 500)
obj2 = Expense_Tracker('23th Feb', 'Salary', 'credit', 30000)
print(obj1.date, obj2.date)
print(obj1.transaction_type)
print(obj2.transaction_type)
