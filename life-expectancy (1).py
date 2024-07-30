i = 0
min_exp = 1000
min_year = ''
min_country = ''
max_exp = -1
max_year = ''
max_country = ''
average = 0
user_year = int(input('Enter year of interest: '))
with open('life-expectancy.csv') as life_files:
    for line in life_files:
        i = i + 1
        line = line.strip()
        parts = line.split(',')
        if i > 1:       
            country = parts[0]
            code = parts[1]
            year = int(parts[2])
            expectancy = float(parts[3])
            if min_exp > expectancy:
                min_exp = expectancy
                min_country = country
                min_year = year

            if max_exp < expectancy:
                max_exp = expectancy
                max_country = country
                max_year = year

print(f'\nThe overall max life expectancy is: {max_exp} from {max_country} in {max_year} ')
print(f'The overall min life expectancy is: {min_exp} from {min_country} in {min_year} ')

if user_year == year:
    

    if min_exp > expectancy:
        min_exp = expectancy
        min_country = country
        min_year = year

    if max_exp < expectancy:

        max_exp = expectancy
        max_country = country
        max_year = year

print(f'\nFor the year {user_year}')
print(f'The average life expectancy across all countries was {average}')
print(f'The max life expectancy was in {max_country} with {max_exp}')
print(f'The min life expectancy was in {min_country} with {min_exp}')

                
