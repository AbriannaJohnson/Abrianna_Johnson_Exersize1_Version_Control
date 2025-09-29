# Abrianna Johnson
# 9/28/25

# This program prompts the user to enter their monthly expenses and
# calculates the highest, lowest, and total expense and displays the data

import functools
from functools import reduce

# Prompts the user for their monthly expenses and
# calculates the total and highest and lowest expenses
def calculate_expenses():
    # Set an accumulator for the expenses
    expenses = []
    print('Enter your monthly expenses')
    print('Type done when finished')
    print('--------------------')

    while True:
        # Prompt the user for type of expense and separate it from the spaces
        expense_type = input('Enter expense type: ').strip()

        # If the user enters the word done convert to lowercase and bring the
        # user to the end of the program
        if expense_type.lower() == 'done':
            break

        while True:
            try:
                # Prompt the user for cost of the expense type
                amount = float(input(f'Enter the amount for {expense_type}: $'))
                if amount < 0:
                    # Prevent the user from entering a negative number
                    print('Amount needs to be a positive number')
                else:
                    print('---------------')
                    # Group the specific expense type to the cost amount and add it to the list expenses
                    expenses.append({'type': expense_type, 'amount': amount})
                    break
            except ValueError:
                # Prevent the user from entering anything other than a number
                print('Amount needs to be a number')

    if not expenses:
        # Prevent the user from typing done before any expenses have been entered
        print('No expenses entered')
        return

    # Calculate the total expense
    total_expense = reduce(lambda acc, expense: acc + expense['amount'], expenses, 0)

    # Find the highest expense
    highest_expense = reduce(lambda acc, expense: expense if expense['amount'] > acc['amount'] else acc, expenses)

    # Find the lowest expense
    lowest_expense = reduce(lambda acc, expense: expense if expense['amount'] < acc['amount'] else acc, expenses)

    # Display the total, highest, and lowest expense
    print("\n----- Total Expenses -----")
    print(f"Total Monthly Expense: ${total_expense:.2f}")
    print(f"Highest Expense: {highest_expense['type']} (${highest_expense['amount']:.2f})")
    print(f"Lowest Expense: {lowest_expense['type']} (${lowest_expense['amount']:.2f})")


if __name__ == "__main__":
    calculate_expenses()


