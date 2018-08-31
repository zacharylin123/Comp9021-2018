# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by *** and Eric Martin for COMP9021


import os
from collections import defaultdict

first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

# Replace this comment with your code




male_sum_per_year = defaultdict(list)
female_sum_per_year = defaultdict(list)

male_final = {}
female_final = {}


for filename in os.listdir(directory):   # calculate sum of each gender
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3: 7])
    female_sum_count = 0
    male_sum_count = 0
    with open(directory + '/' + filename) as file:
        for line in file:           
            gender = line.split(',')[1]
            name = line.split(',')[0]
            count = int(line.split(',')[2])
            if gender == 'F':
                female_sum_count += count 
                female_sum_per_year[year] = female_sum_count   # the sum of every year, female
            else:
                male_sum_count += count
                male_sum_per_year[year] = male_sum_count

# lagerest frequency in which year


for filename in os.listdir(directory):   
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3: 7])
    with open(directory + '/' + filename) as file:
        for line in file:
            
            gender = line.split(',')[1]
            name = line.split(',')[0]
            count = int(line.split(',')[2])
            if gender == 'F':
                if name not in female_final:
                    frequency = count / female_sum_per_year[year]
                    female_final[name] = [year, frequency]
                else:
                    if count / female_sum_per_year[year] > female_final[name][1]:
                        frequency = count / female_sum_per_year[year]
                        female_final[name] = [year, frequency]
            else:
                if name not in male_final:
                    frequency = count / male_sum_per_year[year]
                    male_final[name] = [year, frequency]
                else:
                    if count / male_sum_per_year[year] > male_final[name][1]:
                        frequency = count / male_sum_per_year[year]
                        male_final[name] = [year, frequency]
new_male_final = {}
new_female_final = {}
for name in male_final:
    new_frequency = male_final[name][1] * 100
    new_male_final[name] = [male_final[name][0], new_frequency]

for name in female_final:
    new_frequency = female_final[name][1] * 100
    new_female_final[name] = [female_final[name][0], new_frequency]

           
if first_name in new_female_final:
    female_first_year = new_female_final[first_name][0]
    min_female_frequency = new_female_final[first_name][1]

if first_name in new_male_final:
    male_first_year = new_male_final[first_name][0]
    min_male_frequency = new_male_final[first_name][1]





if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )

