"""
Challenge 17: Hotel Pricing

Calculate a hotel stay cost based on:
- room type
- optional breakfast
- loyalty discount
- minimum price rule
"""

def run():
    room = input("What room size do you need?: ").lower()
    breakfast = input("Would you like to add breakfast?: ").lower()
    loyalty = input("Are you a loyalty member?: ").lower()

    yes_breakfast = (breakfast == "yes")
    yes_loyalty = (loyalty == "yes")

    base_price = (
        80 if room == "single" else
        120 if room == "double" else
        200
    )

    add_breakfast = 15 if yes_breakfast else 0
    loyalty_cost = 0.12 * base_price if yes_loyalty else 0

    cost_for_loyalty = base_price - loyalty_cost
    final_price = cost_for_loyalty + add_breakfast

    final_price = 70 if final_price < 70 else final_price

    print(f"Base price: {base_price}")
    print(f"Breakfast: ${add_breakfast}")
    print(f"Loyalty Discount: {'12%' if yes_loyalty else '0%'}")
    print(f"Total cost for stay: ${final_price:.2f}")

if __name__ == "__main__":
    run()
