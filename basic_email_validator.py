def validate_email(email):

    if len(email) < 6:
        return False

    if not email[0].isalpha():
        return False

    if email.count("@") != 1:
        return False

    if " " in email:
        return False

    for c in email:
        if not (c.isalnum() or c == "." or c == "_" or c == "@"):
            return False

    local, domain = email.split("@")

    if "." not in domain:
        return False

    if len(domain.split(".")[-1]) < 2:
        return False

    return True


while True:
    email = input("Enter your email: ")

    if validate_email(email):
        print("Valid Email")
        break
    else:
        print("Invalid Email")
