"""
Challenge 16: Streaming Plan Pricing

Calculate a streaming subscription cost based on:
- plan type
- optional 4K add-on
- loyalty discount
- minimum price rule
"""

def run():
    plan = input("What plan do you want?: ").lower()
    four_k = input("Do you want 4k option?: ").lower()
    loyalty = input("Are you a long time member?: ").lower()

    yes_4k = (four_k == "yes")
    yes_loyalty = (loyalty == "yes")

    base_price = (
        8 if plan == "basic" else
        12 if plan == "standard" else
        18
    )

    fourk_price = 5 if yes_4k else 0
    loyalty_price = 0.10 * base_price if yes_loyalty else 0

    price_after_loyalty = base_price - loyalty_price
    final_price = price_after_loyalty + fourk_price

    final_price = 7 if final_price < 7 else final_price

    print(f"Base Price: ${base_price}")
    print(f"Discount: {'10%' if yes_loyalty else '0%'}")
    print(f"4k option: ${fourk_price}")
    print(f"Total cost: ${final_price:.2f}")

if __name__ == "__main__":
    run()
