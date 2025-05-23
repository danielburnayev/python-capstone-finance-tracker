# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Program code     Program code     Program code     Program code     Program code     Program code     Program code
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

class EmptyValueError(ValueError):
    pass

class IncorrectInputValueError(ValueError):
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
            print(f"Make sure that when entering input in general, it is not empty/nothing. Give this another shot.\n")
        except ValueError:
            print(f"Make sure that when entering input for the amount, it is a decimal number, not text or anything else. Give this another run.\n")
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
            try:
                print("What would you like to do?\n1. Add Expense\n2. View All Expenses\n3. View Summary\n4. Exit")
                select_num = int(input("Choose an option: "))
                
                if select_num == 1:
                    expense_info = expense_prompt()
                    descr = expense_info[0]
                    category = expense_info[1]
                    amount = expense_info[2]

                    expenses.append({category: (descr, amount)})
                    categories.update({category: categories.get(category) + amount} if (category in categories) else {category: amount})
                elif select_num == 2:
                    view_expenses(expenses)
                elif select_num == 3:
                    view_summary(categories)
                elif select_num == 4:
                    print("Goodbye!\n")
                    break
                else:
                    raise IncorrectInputValueError()
            except IncorrectInputValueError:
                print("Make sure that when selecting from the number options, it is a number from 1-4, nothing else. Give this another try.\n")
            except ValueError:
                print("Make sure that instead of a string or some other value, have it be a number from 1-4. Give this another try.\n")

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