password = input("Enter password: ")

has_uppercase_character = False
has_lowercase_character = False
has_digit_character = False
has_special_character = False

special_characters = "!@#$%^&*"

# Check each character in the password
for character in password:
    if character.isupper():
        has_uppercase_character = True
    elif character.islower():
        has_lowercase_character = True
    elif character.isdigit():
        has_digit_character = True
    elif character in special_characters:
        has_special_character = True

print("\nPassword Validation Result:")

# Display missing conditions
if not has_uppercase_character:
    print("Password must contain at least one uppercase letter.")

if not has_lowercase_character:
    print("Password must contain at least one lowercase letter.")

if not has_digit_character:
    print("Password must contain at least one digit.")

if not has_special_character:
    print("Password must contain at least one special character.")

#length of password
if (len(password)>=8):
    print("password length is sufficent")
else:
    print("password length is not sufficent")    


# Final decision
if has_uppercase_character and has_lowercase_character and has_digit_character and has_special_character and len(password) >=8:
    print("Password is valid ")
else:
    print("Password does not meet minimum security requirements.")
