"""
Challenge 14: Uber Fare Calculator

Calculate a ride fare based on:
- distance
- traffic level
- VIP discount
- minimum fare rule
"""

def run():
    distance = float(input("How many miles is the trip?: "))
    traffic = input("How heavy is the traffic?: ").lower()
    vip = input("Are you a VIP?: ").lower()

    is_vip = (vip == "yes")

    rate_per_mile = (
        1.00 if traffic == "light" else
        1.50 if traffic == "moderate" else
        2.00
    )

    fare = distance * rate_per_mile
    discount = 0.10 * fare if is_vip else 0
    final_fare = fare - discount

    final_fare = 5.00 if final_fare < 5 else final_fare

    print(f"Base rate: ${rate_per_mile:.2f}")
    print(f"Discount: {'10%' if is_vip else '0%'}")
    print(f"Final fare: ${final_fare:.2f}")

if __name__ == "__main__":
    run()
