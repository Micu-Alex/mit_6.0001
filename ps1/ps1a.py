annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) 
total_cost = int(input("Enter the cost of your dream home: "))

portion_down_payment = total_cost * 0.25 #(25%)
current_savings = 0
r = 0.04 #(4%)
monthly_salary = annual_salary / 12 

months = 0
while True:
    monthly_savings = monthly_salary * portion_saved
    current_savings += monthly_savings
    current_savings += current_savings * r/12
    months += 1
    if current_savings  >= portion_down_payment:
        break
    
print(f"Number of months: {months} ")