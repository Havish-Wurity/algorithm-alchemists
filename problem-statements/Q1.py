def calculate_total_bill(amount, tip_percentage):
    total = amount + (amount * tip_percentage / 100)
    return round(total, 2)
amount=float(input('Enter the amount:'))
tip_percentage=float(input('Enter the tip percentage:'))
bill=calculate_total_bill(amount,tip_percentage)
print('''\tOriginal amount:{}\n
\ttip percentage::{}\n
\tThe total bill(including tip):{}'''.format(amount,tip_percentage,bill))
 
