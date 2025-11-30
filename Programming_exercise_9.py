# Abrianna Johnson
# 11/2/25

class BankAcct:
    def __init__(self, name, account_number, initial_balance=0, interest_rate=0.0):
        # Assign the bank account details
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance
        self.interest_rate = interest_rate
        self.interest_earned_on_interest = 0

    def update_interest_rate(self, new_rate):
        if new_rate >= 0:
            # Update the interest rate and prevent negative interest
            self.interest_rate = new_rate
        else:
            print('Interest rate cannot be negative.')

    def deposit(self, amount):
        # Add the amount deposited to the balance
        if amount > 0:
            self.balance += amount
            print(f'Deposited ${amount:.2f}. New balance: ${self.balance:.2f}')
        else:
            # Prevent a negative amount for the deposit
            print('Deposit amount must be positive.')

    def withdraw(self, amount):
        if amount <= 0:
            # Prevent the amount from being a negative number
            print('Withdrawal amount must be a positive number.')
        elif amount > self.balance:
            # Prevent the user from withdrawing more than what they have available
            print('Insufficient funds.')
        else:
            # If the amount is positive and less than the total, subtract the withdrawal from the total
            self.balance -= amount
            # Print the results
            print(f'Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}')

    def get_balance(self):
        # Return the balance after the deposits and withdrawals
        return self.balance

    def calculate_interest(self, num_days):
        # Get the number of days for interest
        if num_days < 0:
            # Make sure the number is positive
            print('Number of days cannot be negative.')
            return

        # Calculate yearly interest rate
        daily_rate = self.interest_rate / 365

        # Calculate the daily interest rate
        interest_for_day = self.balance * daily_rate

        # Calculate interest for the input of number of days
        interest_for_period = interest_for_day * num_days

        # Add the interest earned to the total balance
        self.balance += interest_for_period

        # Calculate the interest earned on the interest for the number of days
        self.interest_earned_on_interest += interest_for_period

        # Print the results
        print(f'Interest of ${interest_for_period:.2f} calculated for {num_days} days.')


    def __str__(self):
        # Display the account information
        return (
            f'Account Name: {self.name}\n'
            f'Account Number: {self.account_number}\n'
            f'Current Balance: ${self.balance:.2f}\n'
            f'Annual Interest Rate: {self.interest_rate:.5%}\n'
            f'Total Interest Earned: ${self.interest_earned_on_interest:.2f}')



def test_account():
    # Print the account information
    print('--- Account ---')
    account1 = BankAcct('Abrianna Johnson', "123456789", 1000, 0.05)
    print(account1)
    print('-----------------------------')

    print('--- Deposits ---')
    # Test making deposits
    account1.deposit(200)
    account1.deposit(100.75)
    # Test a negative deposit
    account1.deposit(-100)
    print('-----------------------------')

    print('--- Withdrawals ---')
    # Test making a withdrawal
    account1.withdraw(500)
    account1.withdraw(20.75)
    # Test a withdrawal with insufficient funds
    account1.withdraw(10000)
    # Test a withdrawal of a negative amount
    account1.withdraw(-10)
    print('-----------------------------')

    print('--- Interest ---')
    # Test updating the interest rate
    account1.update_interest_rate(0.07)
    # Print the results
    print(f'Updated interest rate to: {account1.interest_rate:.2%}')
    # Test new interest rate for a number of days
    account1.calculate_interest(90)
    print('-----------------------------')

    print('--- Test Interest with 0 days ---')
    # Test an invalid number of days
    account1.calculate_interest(0)
    print('-----------------------------')

    print('--- Test Negative Interest Rate ---')
    # Test an invalid interest rate
    account1.update_interest_rate(-0.01)
    print('-----------------------------')

    print('--- Final Account Information ---')
    # Display the final account information after deposits, withdrawals,
    # and interest accumulated
    print(account1)

# Call the test_account function to test the code
test_account()
