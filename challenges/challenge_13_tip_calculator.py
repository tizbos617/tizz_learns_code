"""
Challenge 13: Tip Calculator (Conditional Expressions)

Calculate a tip based on:
- service quality
- whether the customer is a regular
- minimum tip rule for small bills
"""

def run():
    service = input("How was the service?: ").lower()
    bill = float(input("How much was the bill?: "))
    regular = input("Are you a regular?: ").lower()

    tip_percent = (
        25 if service == "excellent" else
        20 if service == "good" else
        15 if service == "okay" else
        10
    )

    is_regular = (regular == "yes")
    bonus = 5 if is_regular else 0

    tip_percent = tip_percent + bonus
    tip_amount = bill * (tip_percent / 100)

    tip_amount = 3 if (bill < 20 and tip_amount < 3) else tip_amount

    print(f"Tip percent: {tip_percent}%")
    print(f"Tip amount: ${tip_amount:.2f}")

if __name__ == "__main__":
    run()
