#libraries needed to run the program
import pandas as pd

#Finance trackking class
class FinanceTracker:
    def __init__(self):
        self.budget = {}
        self.income = 0
        self.expenses = {}
        self.savings = 0
#set budget 
    def set_budget(self, category, amount):
        self.budget[category] = amount
#set income
    def set_income(self, amount):
        self.income = amount
#method to add expense
    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
#method to set saving goals
    def set_savings(self, amount):
        self.savings = amount
#method to generate summary 
    def generate_summary(self):
        summary = f"Income: ${self.income}\n" 
        summary += "Expenses:\n"
        for category, amount in self.expenses.items():
            summary += f"  {category}: ${amount}\n"
        summary += f"Savings Goal: ${self.savings}\n"
        return summary

#Method to save summary to file
    def save_summary(self, filename="data.txt"):
        with open(filename, "w") as file:
            file.write(self.generate_summary())
        print(f"Summary saved to {filename}")
#Subclass for Advanced Finance Tracking
class AdvancedFinanceTracker(FinanceTracker):
    def __init__(self):
        super().__init__()
        self.data = pd.DataFrame(columns=["Category", "Amount"])
#logs expenses into a new catagory
    def log_expense(self, category, amount):
        new_entry = pd.DataFrame({"Category": [category], "Amount": [amount]})
        self.data = pd.concat([self.data, new_entry], ignore_index=True)
#Exports expenses to the file
    def export_expenses(self, filename="expenses.csv"):
        self.data.to_csv(filename, index=False)
        print(f"Expenses saved to {filename}")
     #   Function to interact with user
tracker = AdvancedFinanceTracker()
while True:
        print("\n// Personal Finance Tracker //")
        print("1. Set Income")
        print("2. Add Expense")
        print("3. Set Savings Goal")
        print("4. Generate Summary")
        print("5. Save Summary to File")
        print("6. Export Expenses to CSV")
        print("7. Exit")
        print("//==========================//")
        
        choice = input("Choose an option: ")
        try:
            if choice == "1":
                amount = float(input("Enter income amount: "))
                tracker.set_income(amount)
            elif choice == "2":
                category = input("Enter expense category: ")
                amount = float(input("Enter expense amount: "))
                tracker.add_expense(category, amount)
                tracker.log_expense(category, amount)
            elif choice == "3":
                amount = float(input("Enter savings goal: "))
                tracker.set_savings(amount)
            elif choice == "4":
                print(tracker.generate_summary())
            elif choice == "5":
                tracker.save_summary()
            elif choice == "6":
                tracker.export_expenses()
            elif choice == "7":
                print("Exiting...\n")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a valid number.")
        
