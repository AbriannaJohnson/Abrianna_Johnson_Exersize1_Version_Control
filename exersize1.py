# Abrianna Johnson
# 8/24/25

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
    total_tickets = 10
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