"""
Challenge 15: Membership Pricing

Calculate a membership cost based on:
- membership tier
- student discount
- optional add-on
- minimum price rule
"""

def run():
    membership = input("What membership do you want?: ").lower()
    student = input("Are you a student?: ").lower()
    addon = input("Do you want the addon?: ").lower()

    is_student = (student == "yes")
    is_addon = (addon == "yes")

    base_price = (
        20 if membership == "basic" else
        35 if membership == "standard" else
        50
    )

    add_on = 10 if is_addon else 0
    student_discount = 0.15 * base_price if is_student else 0

    price_after_discount = base_price - student_discount
    final_price = price_after_discount + add_on

    final_price = 15 if final_price < 15 else final_price

    print(f"Base price: ${base_price}")
    print(f"Discount: {'15%' if is_student else '0%'}")
    print(f"Add-on: ${add_on}")
    print(f"Final price: ${final_price:.2f}")

if __name__ == "__main__":
    run()
