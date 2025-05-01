def validate_email(email):
    dots = 0
    at = 0
    domain = False
    for i in range(len(email)):
        if email[i] == '@':
            at +=1
            domain = True
        elif email[i] == '.' and domain:
            dots +=1
    if at == 0:
        raise ValueError('The email must contain one @ symbol.')
    elif at > 1:
        raise ValueError('The email must contain only one @ symbol.')
    if dots == 0:
        raise ValueError("The domain must contain at least one '.' symbol.")

def validate_password(password):
    if len(password)<8:
        raise ValueError('The password must be at least 8 letters long.')
    haslwr = False
    hasupr = False
    hasdgt = False
    for k in password:
        if k.islower():
            haslwr = True
        elif k.isupper():
            hasupr = True
        elif k.isdigit():
            hasdgt = True

    if not haslwr:
        raise ValueError('The password must contain at least one lowercase letter.')
    if not hasupr:
        raise ValueError('The password must contain at least one lowercase letter.')
    if not hasdgt:
        raise ValueError('The password must contain at least one digit.')
try:
    user_email = input("Please enter your email address: ").strip()
    user_password = input("Please enter your password: ").strip()

    validate_email(user_email)
    validate_password(user_password)

    print("Registration successful!")
except ValueError as err:
    print(f"Error: {err}")
