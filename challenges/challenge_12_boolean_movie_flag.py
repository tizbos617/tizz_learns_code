"""
Challenge 12: Movie Theater Entry (Boolean Flag Version)

Determine if the user can enter a movie using boolean flags.
"""

def run():
    sold_out = input("Is the movie sold out? (y/n): ").lower()
    is_sold_out = (sold_out == "y")

    if is_sold_out:
        print("The movie was sold out. Sorry.")
    else:
        ticket = input("Do you have a ticket? (y/n): ").lower()

        if ticket == "y":
            print("Enjoy the movie!")
        else:
            buy = input("Do you want to buy a ticket? (y/n): ").lower()
            buying = (buy == "y")

            if buying:
                print("Thank you for your purchase. Enjoy the movie!")
            else:
                print("Sorry, you cannot come in.")

if __name__ == "__main__":
    run()
