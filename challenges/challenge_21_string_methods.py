# remove leading spaces  lstrip(self, chars=None, /)
# remove trailing rstrip(self, chars=None, /)
# titlecase title(self, /)
# print(help(str))

def run():
    raw_name = input("Please enter your full name: ")
    raw_email = input("Please enter your email: ")
    raw_phone_number = input("Please enter your phone number: ")

    # CLEAN THE NAME
    clean_name = raw_name.strip()
    clean_name = " ".join(clean_name.split())
    formatted_name = clean_name.title()

    # CLEAN THE EMAIL
    email = raw_email.strip().lower()

    if email.count("@") != 1:
        print("Invalid email: must contain exactly one '@'")
        return

    at_index = email.find("@")
    dot_index = email.find(".", at_index)

    if dot_index == -1:
        print("Invalid email: must contain a '.' after the '@'")
        return

    # CLEAN THE PHONE NUMBER
    phone_number = (
        raw_phone_number
            .replace(" ", "")
            .replace("-", "")
            .replace("(", "")
            .replace(")", "")
    )

    if not phone_number.isdigit():
        print("Invalid phone number: must contain only digits")
        return

    if len(phone_number) != 10:
        print("Invalid phone number: must be exactly 10 digits")
        return

    print("\nContact saved!")
    print(f"Name:  {formatted_name}")
    print(f"Email: {email}")
    print(f"Phone: {phone_number}")
if __name__ == "__main__":
    run()





