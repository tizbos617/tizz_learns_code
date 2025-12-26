"""
Challenge 04: Movie Theater Entry

Determine if a user can enter a movie based on:
- whether the movie is sold out
- whether they have a ticket
- whether they want to buy one
"""

def run():
    sold_out = input("Is the movie sold out? (y/n): ").lower()
    is_sold_out = (sold_out == "y")

    if is_sold_out:
        print("The movie is sold out. Sorry.")
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
