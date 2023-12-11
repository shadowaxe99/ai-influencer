class Budget:
self.initial_budget = initial_budget
self.expenses = []
self.income = []
def add_expense(self, amount):
"""Add an expense to the budget."""
self.expenses.append(amount)
def add_income(self, amount):
"""Add income to the budget."""
self.income.append(amount)
def calculate_total(self):
"""Calculate the total budget."""
total_expenses = sum(self.expenses)
total_income = sum(self.income)
return self.initial_budget + total_income - total_expenses