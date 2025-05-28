import pandas as pd

data = pd.read_excel('Nepal_Census_Data_2008BS_to_2078BS.xlsx')

ui = input('Write what you want to see: ').lower().strip()

def population_greater():
    pop_greater = int(input("Write the population you want it to be greater than: "))
    filtered_data = data[data['Total Population'] > pop_greater]
    print(f"\nYears in which Nepal's population was more than {pop_greater}:")
    print(filtered_data[['Census Year (BS)', 'Total Population']])

def population_smaller():
    pop_smaller = int(input("Write the population you want it to be smaller than: "))
    filtered_data = data[data['Total Population'] < pop_smaller]
    print(f"\nYears in which Nepal's population was less than {pop_smaller}:")
    print(filtered_data[['Census Year (BS)', 'Total Population']])

def woman_pop():
    year = int(input('Type the year (BS) you want the population of women for: '))
    filtered_row = data[data['Census Year (BS)'] == year]
    if not filtered_row.empty:
        female_population = filtered_row.iloc[0]['Female Population']
        print(f"\nNepal's female population in the year {year}: {female_population}")
    else:
        print("No data found for that year.")

def man_pop():
    year = int(input('Type the year (BS) you want the population of men for: '))
    filtered_row = data[data['Census Year (BS)'] == year]
    if not filtered_row.empty:
        male_population = filtered_row.iloc[0]['Male Population']
        print(f"\nNepal's male population in the year {year}: {male_population}")
    else:
        print("No data found for that year.")

def child_pop():
    year = int(input('Type the year (BS) you want the population of children for: '))
    filtered_row = data[data['Census Year (BS)'] == year]
    if not filtered_row.empty:
        child_population = filtered_row.iloc[0]['Child Population']
        print(f"\nNepal's child population in the year {year}: {child_population}")
    else:
        print("No data found for that year.")

def employed_pop():
    year = int(input('Type the year (BS) you want the employed population for: '))
    filtered_row = data[data['Census Year (BS)'] == year]
    if not filtered_row.empty:
        employed_population = filtered_row.iloc[0]['Employed Population']
        print(f"\nNepal's employed population in the year {year}: {employed_population}")
    else:
        print("No data found for that year.")

# Match input to function
match ui:
    case 'census in which population is greater than':
        population_greater()
    case 'census in which population is smaller than':
        population_smaller()
    case 'woman population':
        woman_pop()
    case 'man population':
        man_pop()
    case 'child population':
        child_pop()
    case 'employed population':
        employed_pop()
    case _:
        print("Invalid input. Try something like: woman population, man population, etc.")

    






