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
    

def exec_finance_tracker():
    expenses = []
    while True:
        expense_info = expense_prompt()
        descr = expense_info[0]
        category = expense_info[1]
        amount = expense_info[2]

        expenses.append({category: (descr, amount)})
        print(f"Added the following expense:\n\tCategory: {category}\n\tDescription: {descr}\n\tAmount: {amount}\n")


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