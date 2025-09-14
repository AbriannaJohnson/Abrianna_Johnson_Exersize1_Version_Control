# Abrianna Johnson
# 8/24/25

# Program description:
# This program allows buyers to purchase a limited amount of
# tickets to a cinema, and displays the number of tickets
# remaining after each purchase



# Function 1: get_tickets_from_buyer()

# Description: This function creates a loop for the user to keep
# giving an input for the number of tickets they want to buy until
# all tickets have been sold. It also limits the user to 1 to 4 tickets,
# and makes the user enter a number as a value.

# Parameters: None

# Variables: num_tickets - holds the number of tickets the buyer wants

# Logical steps:
# 1. create a variable that holds the input from the buyer
# 2. if the input is between 1 and 4 it returns the number
# 3. if the input is not in that range, a message pops up and starts the loop again
# 4. if the input is not a number, a message pops up and restarts the loop

# Returns: num_tickets - returns a number that is within the requirements



# Function 2: sell_tickets()

# Description: This function keeps track of the number of tickets sold,
# subtracts it from the total until all tickets sell and the loop ends

# Parameters: None

# Variables:
# 1. total_tickets - a hardcoded number of tickets available from the start
# 2. tickets_left - keeps track of the tickets after a purchase
# 3. num_buyers - an accumulator for the number of purchases
# 4. tickets_wanted - calls the get_tickets_from_buyer() function to start
#                     the loop and creates a variable that can be subtracted from the total

# Logical steps:
# 1. Create a variable that holds the hardcoded number of tickets
# 2. Set the tickets left after a purchase to equal total tickets
# 3. Display the number to the user
# 4. Create a loop that restarts until all tickets are sold
# 5. create an instance of the get_tickets_from_buyer() function
# 6. Subtract tickets wanted from tickets available and add one to the number of buyers
# 7. Print messages that display the number of buyers and that all tickets have been sold.

# Returns: None


def get_tickets_from_buyer():
    while True:
        try:
            num_tickets = int(input('Enter the number of tickets you want to purchase: '))
            # Gets an input from the user
            if 1 <= num_tickets <= 4:
                # Limit the user to up to 4 tickets
                return num_tickets
            else:
                print('You can only buy up to 4 tickets')
        except ValueError:
            print('Enter a number')


def sell_tickets():
    total_tickets = 20
    tickets_left = total_tickets
    # The tickets left will equal the total tickets after a user purchases tickets
    num_buyers = 0
    # Set an accumulator for number of buyers
    print(f'Total tickets available for pre-sale: {total_tickets}')
    while tickets_left > 0:
        print(f'{tickets_left} tickets still available')
        tickets_wanted = get_tickets_from_buyer()
        # Calls the get_tickets_from_buyer() function to start the loop
        if tickets_wanted <= tickets_left:
            tickets_left -= tickets_wanted
            # Subtracts the tickets wanted from the total number available
            num_buyers += 1
            # Adds 1 to the accumulator
        else:
            print(f'Only {tickets_left} tickets are available')

    print('All tickets have been sold!')
    print(f'Total number of buyers: {num_buyers}')
sell_tickets()
# Start the loop

# Link to repository: