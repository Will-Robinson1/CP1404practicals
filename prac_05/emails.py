"""
Emails
Estimate: 45 minutes
Actual:   25 minutes
"""

def main():
    email_to_name = {}
    get_email = input("Email: ")
    while get_email != "":
        user_name = get_name_from_email(get_email)
        is_correct = input(f"Is your name {user_name}? (y/n) ").lower()
        if is_correct == 'n' or is_correct == 'no':
            get_correct_name = input("Name: ")
            email_to_name[get_email] = get_correct_name
        elif is_correct == 'y' or is_correct == 'yes' or is_correct == '':
            email_to_name[get_email] = user_name
        get_email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email: str) -> str:
    """Infer a nicely formatted name from an email address."""
    name = email.split("@", 1)[0]
    for sep in [".", "_", "-"]:
        name = " ".join(name.split(sep))
    return name.title()
main()