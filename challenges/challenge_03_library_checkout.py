"""
Challenge 03: Library Checkout

Determine if a user can check out a book based on:
- whether the library is closed
- whether they have a library card
- whether they want to sign up
"""

def run():
    closed = input("Is the library closed? (yes or no): ").lower()
    is_closed = (closed == "yes")

    if is_closed:
        print("The library is closed. You cannot check out books.")
    else:
        do_you_have_a_card = input("Do you have a library card? (yes or no): ").lower()
        has_card = (do_you_have_a_card == "yes")

        if has_card:
            print("You may check out a book.")
        else:
            want_to_sign_up = input("Do you want to sign up for a card? (yes or no): ").lower()
            sign_up = (want_to_sign_up == "yes")

            if sign_up:
                print("You have signed up. You may now check out a book.")
            else:
                print("You cannot check out books without a library card.")

if __name__ == "__main__":
    run()
