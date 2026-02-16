def convert_temperature(value, unit):
    if unit == 'C':
        # Celsius to Fahrenheit
        result = (value * 9/5) + 32
        return round(result, 1)
    
    elif unit == 'F':
        # Fahrenheit to Celsius
        result = (value - 32) * 5/9
        return round(result, 1)
    
    else:
        return "Invalid Unit"
