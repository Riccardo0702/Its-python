def validate_password(password):
    if len(password) < 20:
        raise Exception("Invalid password.")
    for i in password:
        if i