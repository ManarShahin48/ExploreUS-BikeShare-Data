from re import M
from this import d
import pandas as pd
import time


Month = {	
    'Jan': 1,
	'Feb': 2,
	'March': 3,
	'April': 4,
	'May': 5,
	'June': 6,
	'July': 7,
	'Aug': 8,
	'Sept': 9,
	'Octo': 10,
	'Nov': 11,
	'Dec': 12		
}

Day = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5, 
    'Sunday': 6,
}

CITY_DATA = { 
    'chicago': 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv' 
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('♦'*60)
    print('Hello! Let\'s explore some US bikeshare data!')
    print('♦'*60)
    while True:
        city = input("Please, enter the city (chicago, new york, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Not excist, please enter the right city")
    print('-'*40)

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please, enter the month(All, Jan, Feb, March, April, May, june): ").title()
        if month in Month or month == 'All':
            break
        else:
            print("Not excist, please enter the right month")
    print('-'*40)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please, enter the day(All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ").title()
        if day in Day or day == 'All':
            break
        else:
            print("Not excist, please enter the right day")

    print('-'*40)
    return city, month, day
    

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()


    ########### Filter for the Month ###########
    if month != 'All':    
        df = df[df['Month'] == Month[month]]

    ########### Filter for the Day ###########
    if day != 'All':    
        df = df[df['Day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # display the most common month
    list_of_key = list(Month.keys())
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    common_month = df['Month'].mode().iloc[0]
    print('Most Popular Month:', list_of_key[common_month - 1])
    print('-'*40)
    
    # display the most common day of week
    common_day = df['Day'].mode()[0]
    print('Most Popular Day:', common_day)
    print('-'*40)

    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    popular_hour = df['Hour'].mode()[0]
    if(popular_hour > 12):
        print('Most Popular Start Hour:', popular_hour - 12)
    else:
        print('Most Popular Start Hour:', popular_hour)
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', common_start_station)
    print('-'*40)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', common_end_station)
    print('-'*40)

    # display most frequent combination of start station and end station trip
    the_combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print(the_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    sum = df['Trip Duration'].sum()     
    print('The total travel time is = ', sum)
    print('-'*40)

    # display mean travel time
    mean = df["Trip Duration"].mean()
    print('The mean travel time is = ',mean)
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    print('-'*40)

    # Display counts of gender
    gender = df['Gender'].value_counts()
    print(gender)
    print('-'*40)

    # Display earliest year of birth
    earliest = min(df['Birth Year'])
    print('The earliest year is: ', int(earliest))

    # Most recent year of birth
    most_recent = max(df['Birth Year'])
    print('The most recent year is: ', int(most_recent))

    # Most common year of birth
    common_year = df['Birth Year'].mode()[0]
    print('Most common year of birth:', int(common_year))
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data == 'Yes' or view_data == 'yes' or view_data == 'YES'):
        print(df.iloc[start_loc : start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city == 'chicago' or city == 'new york':
            user_stats(df)
        
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
