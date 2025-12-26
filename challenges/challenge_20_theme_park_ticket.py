"""
Challenge 20: Theme Park Ticket Pricing (Capstone)

Calculate the total cost of a theme park ticket based on:
- ticket type (child, adult, senior)
- optional meal plan
- optional fastpass
- local resident discount
- minimum price rule
"""

def run():
    ticket = input("Is the ticket for a child, adult, or senior? ").lower()
    meals = input("Do you want the meal plan? (yes or no): ").lower()
    fastpass = input("Do you want the fastpass? (yes or no): ").lower()
    local = input("Are you a local? (yes or no): ").lower()

    yes_meals = (meals == "yes")
    yes_fastpass = (fastpass == "yes")
    yes_local = (local == "yes")

    ticket_price = (
        40 if ticket == "child" else
        70 if ticket == "adult" else
        50
    )

    meal_plan_cost = 15 if yes_meals else 0
    fastpass_cost = 30 if yes_fastpass else 0

    resident_discount = 0.08 * ticket_price if yes_local else 0
    price_after_discount = ticket_price - resident_discount

    final_cost = price_after_discount + meal_plan_cost + fastpass_cost
    final_cost = 35 if final_cost < 35 else final_cost

    print(f"Your ticket cost is ${ticket_price:.2f}.")
    print(f"Resident discount is ${resident_discount:.2f}.")
    print(f"Meal plan cost is ${meal_plan_cost:.2f}.")
    print(f"Fastpass cost is ${fastpass_cost:.2f}.")
    print(f"Total cost is ${final_cost:.2f}.")

if __name__ == "__main__":
    run()
