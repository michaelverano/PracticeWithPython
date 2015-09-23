from decimal import *

def compoundMoultiplier(starting_figure, rate, years):	
	years_to_months = years * 12 * 22 #30 days minus weekends, so 22 days average for the weekdays.
	rate_to_percent = rate/100.0

	for time in range(years_to_months):
		
		monthly_compound = starting_figure*(time + 1)*rate_to_percent + starting_figure

		print('Day: ' + str(time + 1) + ', Amount: ' + str(monthly_compound))


while True:
	print('What is your starting figure?')
	starting_figure = input('Starting Figure: ')

	if starting_figure == '':
		break

	print(r'What is the % rate you want to compound?')
	rate =  input('Percentage Rate: ')

	if rate == '':
		break

	print('How many years?')
	years = input('Years: ')
	
	if years == '':
		break

	compoundMoultiplier(starting_figure, rate, years)