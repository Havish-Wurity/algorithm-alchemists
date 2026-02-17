def convert_seconds(total_seconds):
    if total_seconds>=86400:
    print('The total number of seconds exceeded to that of a day')
elif total_seconds<0:
    print('the total number of seconds are invalid.Please enter valid number of seconds')
 else:
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    
    return '{}m {}s'.format(minutes,seconds)   
    




   
