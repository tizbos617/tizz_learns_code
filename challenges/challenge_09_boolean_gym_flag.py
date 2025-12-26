"""
Challenge 09: Gym Entry (Boolean Flag Version)

Determine if the user can enter the gym using boolean flags.
"""

def run():
    closed = input("Is the gym closed? (yes or no): ").lower()
    is_closed = (closed == "yes")

    if is_closed:
        print("The gym is closed and you cannot enter.")
    else:
        are_you_member = input("Are you a member already? (yes or no): ").lower()
        is_member = (are_you_member == "yes")

        if is_member:
            print("You may enter.")
        else:
            day_pass = input("Do you have a day pass? (yes or no): ").lower()
            has_pass = (day_pass == "yes")

            if has_pass:
                print("You may enter.")
            else:
                print("You need to sign up.")

if __name__ == "__main__":
    run()
