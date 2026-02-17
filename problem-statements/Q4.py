def get_ticket_price(age,is_student):
    if age>0 and age<=120:
        if age<12:
            return 8
        elif age>=12 and age<=64:
            if is_student==True:
                return 12
            else:
                return 15
        elif age>=65:
            return 10
    else:
        return 0

 
if ticket_price==0:
    print('Please enter a valid age')
else:
    print('The price of the ticket:$',ticket_price)
