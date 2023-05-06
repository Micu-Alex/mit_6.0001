annual_salary = float(input("Enter the starting salary: "))
monthly_salary = annual_salary / 12 

semiannual = .07
total_cost = 1000000
down_payment_rate = 0.25 #(25%)
anual_return = 0.04 #(4%)
months = 36
epsilon = 100
steps = 0

# Calculate the current savings after a certain number of months
def calc_current_savings(monthly_salary, savings_rate, months):
    current_savings = 0 
    while months > 0:
        monthly_savings = monthly_salary * savings_rate
        current_savings += monthly_savings
        current_savings += current_savings * anual_return/12
        months -= 1
        if months % 6 == 0:
            monthly_salary += monthly_salary * semiannual
    return current_savings

# Checks if down payment is within desired range
def within_epsilon(current_savings, total_cost, epsilon):
    return abs(current_savings - total_cost * 0.25) <= epsilon

# Uses bisection search to find the best savings rate
def bisect_search( down_payment_rate, months, epsilon):
    global steps
    high = 10000
    low = 0
    savings_rate = (high + low) / 2.0
    
    while True:
        current_savings = calc_current_savings(monthly_salary, savings_rate, months)
        if within_epsilon(current_savings, total_cost, epsilon):
               return savings_rate
        elif current_savings < total_cost * down_payment_rate:
            low = savings_rate
        else:
            high = savings_rate
       
        savings_rate = (high + low) / 2.0
        steps += 1

# Check if it is possible to pay the down payment in three years
current_savings = calc_current_savings(monthly_salary, 1.0, months)
if current_savings < total_cost * down_payment_rate:
    print("It is not possible to pay the down payment in three years.")
else:
    result = bisect_search(down_payment_rate, months, 100)
    print(f"Best savings rate: {round(result, 4)}")
    print(f"Steps in bisection search: {steps}")