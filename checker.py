def check_length(password):
    characters_req = 12 - len(password)
    if characters_req <= 0:
        return "Checked"
    else:
        return "Length: Oops! Too short add {} more elements".format(characters_req)
    
def check_complexity(password):
    # Return message if password contains at least 1 lowercase, 1 uppercase, 1 number, 1 symbol
    
    has_lowercase = False
    has_uppercase = False
    has_numbers = False
    has_symbols = False
    
    complexity_symbols = [has_lowercase, has_uppercase, has_numbers, has_symbols]
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_numbers = True
        elif char in "!@#$%^&*_-/?~":
            has_symbols = True

    if has_lowercase and has_uppercase and has_numbers and has_symbols is True:
        return "Checked"
     
    if char.islower() is False:
        return "add a lowercase element."
    if char.isupper() is False:
        return "add an uppercase element."
    if char.isdigit() is False:
        return "Add a number."
    if char in "!@#$%^&*_-/?~" == False:
        return "Add on of these !@#$%^&*_-/?~"

    

    

    
          
    