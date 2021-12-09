from datetime import date

todays_date = date.today()

current_year = todays_date.year
current_month = todays_date.month
current_day = todays_date.day

birth_year = input( 'birth year: ' )
birth_month  = input( 'birth month: ' )
birth_day  = input( 'birth day: ' )

age_year = current_year- int(birth_year)
age_month  = current_month - int(birth_month)
age_day =  current_day - int(birth_day)

print(f'you are {age_year} year ,{age_month} months , {age_day} days old ')
