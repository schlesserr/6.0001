annual_salary = float(input('enter your annual salary: '))
portion_saved = float(input('How much you will saved as a decimal [10% = 0.1]: '))
total_cost = float(input('How much cost your dream home? 	'))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal [10% = 0.1]: '))

month_salary = annual_salary / 12
portion_down_payment = 0.25
current_savings = 0
r = 0.04
month = 0

while current_savings <= (portion_down_payment * total_cost):
	current_savings += (portion_saved * month_salary) + (current_savings * r)/12
	month += 1
	if (month % 6) == 0:
		month_salary *= (semi_annual_raise + 1)
	
print('Number of months:', month)
