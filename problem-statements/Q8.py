def sanitize_email(raw_input):
    if not isinstance(raw_input, str):
        return "invalid email"
    
    email = raw_input.strip().lower()
    
    email = email.replace(" ", "")
    
    if email.count("@") != 1:
        return "invalid email"
    
    local, domain = email.split("@")
    
    if not local or not domain:
        return "invalid email"
    
    if "." not in domain:
        return "invalid email"
    
    return email
