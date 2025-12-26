"""
Challenge 10: Concert Entry (Boolean Flag Version)

Determine if the user can enter a concert using boolean flags.
"""

def run():
    sold_out = input("Is the venue sold out? (yes or no): ").lower()
    is_sold_out = (sold_out == "yes")

    if is_sold_out:
        print("The venue is sold out. You cannot enter.")
    else:
        have_ticket = input("Do you have a ticket? (yes or no): ").lower()
        has_ticket = (have_ticket == "yes")

        if has_ticket:
            print("You can enter. Enjoy the concert!")
        else:
            buy = input("Do you want to buy a ticket? (yes or no): ").lower()
            will_buy = (buy == "yes")

            if will_buy:
                print("Here is your ticket. Enjoy the concert!")
            else:
                print("No ticket, no show.")

if __name__ == "__main__":
    run()
