"""
Challenge 19: Airline Ticket Pricing

Calculate a flight ticket cost based on:
- seat class
- checked bags
- priority boarding
- frequent flyer discount
- minimum price rule
"""

def run():
    seat = input("What seat class do you want?: ").lower()
    bags = input("Do you have any bags?: ").lower()
    priority = input("Is this priority?: ").lower()
    frequent = input("Are you a frequent flyer?: ").lower()

    is_priority = (priority == "yes")
    is_frequent = (frequent == "yes")
    has_bag = (bags == "yes")

    base_ticket_price = (
        150 if seat == "economy" else
        250 if seat == "premium" else
        400
    )

    checked_bag_price = 35 if has_bag else 0
    priority_charge = 20 if is_priority else 0
    frequent_flyer_discount = 0.10 * base_ticket_price if is_frequent else 0

    final_cost = base_ticket_price + checked_bag_price + priority_charge - frequent_flyer_discount
    final_cost = 120 if final_cost < 120 else final_cost

    print(f"Ticket cost: ${base_ticket_price}")
    print(f"Bag charge: ${checked_bag_price}")
    print(f"Priority charge: ${priority_charge}")
    print(f"Frequent flyer discount: ${frequent_flyer_discount:.2f}")
    print(f"Total: ${final_cost:.2f}")

if __name__ == "__main__":
    run()
