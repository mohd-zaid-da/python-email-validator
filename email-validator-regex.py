import re

def validate_email(email):
    email_condition = r"^[A-Za-z][A-Za-z0-9_.]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(email_condition, email) is not None


if __name__ == "__main__":
    user_email = input("Enter Your Mail: ").strip()

    if validate_email(user_email):
        print("✅ Valid Email")
    else:
        print("❌ Invalid Email")
