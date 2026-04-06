def check_length(password):
    if len(password) >=12:
        return "Checked"
    else:
        return "Length: Oops! Too short like your dih"
    
def check_complexity(password):
    # Return message if password contains at least 1 lowercase, 1 uppercase, 1 number, 1 symbol
    has_lowercase = False
    has_uppercase = False
    has_numbers = False
    has_symbols = False

    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_numbers = True
        elif char in "!@#$%^&*_-/?~":
            has_symbols = True

    if has_lowercase and has_uppercase and has_numbers and has_symbols:
        return "Checked"
    else:
        return "Complexity: Weaker than your game bruh..."
          
    