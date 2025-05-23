# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Program code     Program code     Program code     Program code     Program code     Program code     Program code
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

class EmptyValueError(ValueError):
    pass

def check_for_empty(given_str):
    return len(given_str) == 0

def expense_prompt():
    good_inputs = 0
    
    while True:
        try:
            if good_inputs == 0:
                descr = input("Enter expense description: ")
                if check_for_empty(descr):
                    raise EmptyValueError()
                good_inputs += 1

            if good_inputs == 1:
                category = input("Enter category: ")
                if check_for_empty(category):
                    raise EmptyValueError()
                good_inputs += 1

            if good_inputs == 2:
                amount = input("Enter amount: ")
                if check_for_empty(amount):
                    raise EmptyValueError()
                amount = float(amount)
            
        except EmptyValueError:
            print(f"Make sure that when entering input in general, it is not empty/nothing. Give it another shot.\n")
        except ValueError:
            print(f"Make sure that when entering input for the amount, it is a decimal number, not text or anything else. Give it another try.\n")
        else:
            print("Expense added successfully.\n")
            return descr, category, amount

def view_expenses(data):
    for expense in data:
        for category, info in expense.items():
            print(f"Category: {category}\n\t- {info[0]}: ${info[1]:.2f}\n")

def view_summary(data):
    print("Summary:")
    for category, amount in data.items():
        print(f"{category}: ${amount:.2f}")

def exec_finance_tracker():
    expenses = []
    categories = {}
    while True:
        expense_info = expense_prompt()
        descr = expense_info[0]
        category = expense_info[1]
        amount = expense_info[2]

        expenses.append({category: (descr, amount)})
        categories.update({category: categories.get(category) + amount} if (category in categories) else {category: amount})

        view_expenses(expenses)
        view_summary(categories)

def start_program():
    print("Welcome to the personal finance tracker!\n")
    exec_finance_tracker()


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Runner code     Runner code     Runner code     Runner code     Runner code     Runner code     Runner code     Runner code
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

if __name__ == "__main__":
    start_program()