"""
Challenge 18: Car Rental Pricing

Calculate a rental cost based on:
- car type
- optional insurance
- under-25 surcharge
- minimum price rule
"""

def run():
    car = input("What kind of car do you need?: ").lower()
    insurance = input("Do you want insurance?: ").lower()
    under_25 = input("Are you under 25?: ").lower()

    want_insurance = (insurance == "yes")
    is_under_25 = (under_25 == "yes")

    base_rental_price = (
        30 if car == "economy" else
        45 if car == "standard" else
        70
    )

    insurance_price = 20 if want_insurance else 0
    under_25_charge = 0.15 * base_rental_price if is_under_25 else 0

    final_price = base_rental_price + under_25_charge + insurance_price
    final_price = 40 if final_price < 40 else final_price

    print(f"Base price: {base_rental_price}")
    print(f"Insurance charge: {insurance_price}")
    print(f"Under 25 charge: ${under_25_charge:.2f}")
    print(f"Final price: ${final_price:.2f}")

if __name__ == "__main__":
    run()
