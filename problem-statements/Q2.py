def convert_seconds(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    
    return minutes,seconds

total_seconds=int(input('Enter the number of seconds:'))
if total_seconds>=86400:
    print('The total number of seconds exceeded to that of a day')
elif total_seconds<0:
    print('the total number of seconds are invalid.Please enter valid number of seconds')
else:
    minutes,seconds=convert_seconds(total_seconds)
    print('{}m {}s'.format(minutes,seconds))
