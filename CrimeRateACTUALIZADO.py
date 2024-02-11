import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Public.csv')

def print_menu():
    print('Please select an option:')
    print('1. Crime rate by region (Region_2013_label)')
    print('2. Crime rate by urban area (Urban_area_2013_label)')
    print('3. Crime rate by type of crime (Area_unit_2013_label)')
    print('4. Crime rate by Urban Area Type (Urban_area_type)')
    print('5. Crime rate by Territorial Authority Area (Territorial_authority_area_2013_label)')
    print('6. Total Victimisations in 2015')
    print('7. Total Population in 2015')
    print('8. Average Rate per 10,000 Population')
    print('9. Rate Ratio to NZ Average Rate')
    print('10. Exit')

def generate_option(choice):
    if choice == 1:
        df['Crime Rate'] = df['Victimisations_calendar_year_2015'] / (df['Population_mid_point_2015'] / 10000)
        df.groupby('Region_2013_label')['Crime Rate'].mean().plot(kind='bar')
        plt.xlabel('Region')
        plt.ylabel('Average Crime Rate (per 10,000 population)')
        plt.title('Crime rate by region in New Zealand, 2015')
        plt.show()
    elif choice == 2:
        df['Crime Rate'] = df['Victimisations_calendar_year_2015'] / (df['Population_mid_point_2015'] / 10000)
        df.groupby('Urban_area_2013_label')['Crime Rate'].mean().plot(kind='bar')
        plt.xlabel('Urban area')
        plt.ylabel('Average Crime Rate (per 10,000 population)')
        plt.title('Crime rate by urban area in New Zealand, 2015')
        plt.show()
    elif choice == 3:
        df['Crime Rate'] = df['Victimisations_calendar_year_2015'] / (df['Population_mid_point_2015'] / 10000)
        df.groupby('Area_unit_2013_label')['Crime Rate'].mean().plot(kind='bar')
        plt.xlabel('Type of crime')
        plt.ylabel('Average Crime Rate (per 10,000 population)')
        plt.title('Crime rate by type of crime in New Zealand, 2015')
        plt.xticks(rotation=45)
        plt.show()
    elif choice == 4:
        df['Crime Rate'] = df['Victimisations_calendar_year_2015'] / (df['Population_mid_point_2015'] / 10000)
        df.groupby('Urban_area_type')['Crime Rate'].mean().plot(kind='bar')
        plt.xlabel('Urban Area Type')
        plt.ylabel('Average Crime Rate (per 10,000 population)')
        plt.title('Crime rate by Urban Area Type in New Zealand, 2015')
        plt.show()
    elif choice == 5:
        df['Crime Rate'] = df['Victimisations_calendar_year_2015'] / (df['Population_mid_point_2015'] / 10000)
        df.groupby('Territorial_authority_area_2013_label')['Crime Rate'].mean().plot(kind='bar')
        plt.xlabel('Territorial Authority Area')
        plt.ylabel('Average Crime Rate (per 10,000 population)')
        plt.title('Crime rate by Territorial Authority Area in New Zealand, 2015')
        plt.xticks(rotation=45)
        plt.show()
    elif choice == 6:
        total_victimisations = df['Victimisations_calendar_year_2015'].sum()
        print(f'Total Victimisations in 2015: {total_victimisations}')
    elif choice == 7:
        total_population = df['Population_mid_point_2015'].sum()
        print(f'Total Population in 2015: {total_population}')
    elif choice == 8:
        average_rate = (df['Victimisations_calendar_year_2015'] / (df['Population_mid_point_2015'] / 10000)).mean()
        print(f'Average Rate per 10,000 Population: {average_rate}')
    elif choice == 9:
        rate_ratio = df['Rate_ratio_NZ_average_rate'].mean()
        print(f'Rate Ratio to NZ Average Rate: {rate_ratio}')
    elif choice == 10:
        exit()
    else:
        print('Invalid choice.')

def main():
    while True:
        print_menu()

        choice = int(input('Enter your choice: '))

        generate_option(choice)

main()
