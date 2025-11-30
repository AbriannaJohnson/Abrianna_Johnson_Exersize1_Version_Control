# Abrianna Johnson
# 11/30/25


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import random

# Create the database where the populations are saved
database = 'population_AJ.db'

def setup_database():
    # Create the database and table and insert the 2023 population data
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

# Create the table
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS population (
                city TEXT,
                year INTEGER,
                population INTEGER,
                PRIMARY KEY (city, year)
            )
        ''')
# Initial 2023 data for population of cities in florida
    initial_data = [
        ('Bradenton', 2023, 56300),
        ('Jacksonville', 2023, 985843),
        ('Miami', 2023, 455924),
        ('Tampa', 2023, 413704),
        ('Orlando', 2023, 320742),
        ('St. Petersburg', 2023, 263353),
        ('Tallahassee', 2023, 202221),
        ('Fort Lauderdale', 2023, 184255),
        ('Brandon', 2023, 116365),
        ('Boca Raton', 2023, 102238),
        ]
# Insert the initial data and ignore if a city or year already exists
    cursor.executemany('INSERT OR IGNORE INTO population (city, year, population) VALUES (?,?,?)',
                       initial_data)

    conn.commit()
    conn.close()


def population_change():
    # Simulate population growth or decline for the next 20 years
    conn = sqlite3.connect(database)

    # Get the list of cities stored in the database
    cities_df = pd.read_sql_query("SELECT DISTINCT city FROM population", conn)
    cities = cities_df['city'].tolist()


    new_data = []
    # Assign the start year and end year for the simulation
    start_year = 2024
    end_year = 2043


    for city in cities:
        # Get the starting 2023 population to start the simulation
        current_pop_df = pd.read_sql_query(f"SELECT population FROM population WHERE city = '{city}' AND year = 2023", conn)
        current_pop = current_pop_df['population'].iloc[0]

        for year in range(start_year, end_year + 1):
            # simulate growth or decline between -2% and +4%
            rate = random.uniform(-0.02, 0.04)
            current_pop = int(current_pop * (1 + rate))

            new_data.append((city, year, current_pop))

    # Insert all of the simulated data
    conn.executemany("INSERT OR IGNORE INTO population (city, year, population) VALUES (?,?,?)", new_data)
    conn.commit()
    conn.close()
    print(f'Population simulated and inserted for years {start_year} through {end_year}.')


def display_population_growth():
    # ask the user to choose a city and display the population growth using matplotlib
    conn = sqlite3.connect(database)
    cities_df = pd.read_sql_query("SELECT DISTINCT city FROM population ORDER BY city", conn)
    cities = cities_df['city'].tolist()

    print('\nCities for population display:')
    # Display the cities to the user
    for i, city in enumerate(cities):
        print(f'{i + 1}. {city}')


# Prompt the user for their choice of city to visualize
    choice = input(f'Enter the number of the city you want to visualize (1-10): ')

    try:
        city_index = int(choice) - 1
        selected_city = cities[city_index]
    except (ValueError, IndexError):
        print('Invalid choice')
        conn.close()
        return

    # Get all of the population data for the selected city
    pop_data_df = pd.read_sql_query(f"SELECT year, population FROM population WHERE city = '{selected_city}' ORDER BY year", conn)
    conn.close()

    # Create the visualization using matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(pop_data_df['year'], pop_data_df['population'], marker='o', linestyle='-', color='b')
    plt.title(f'Population Growth/Decline for {selected_city} (2023-2043)')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.xticks(pop_data_df['year'][::2], rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Call each function to start the simulation
    setup_database()
    population_change()
    display_population_growth()