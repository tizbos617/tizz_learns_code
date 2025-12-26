"""
Challenge 05: Trip Decision (3D)

Determine whether the user should take a trip based on:
- weather conditions
- gas level
- whether a friend is available
- budget amount
"""

def run():
    weather = input("What is the weather like? (sunny, cloudy, or rainy): ").lower()
    gas_level = int(input("What % of gas do you have?: "))
    friend_available = input("Do you have a friend available? yes/no: ").lower()
    budget = int(input("How much do you have for the trip?: "))

    friend_is_available = (friend_available == "yes")

    if (
        (weather == "sunny" and gas_level >= 50) or
        (budget >= 100 and friend_is_available) or
        ((weather == "cloudy" or gas_level >= 75) and friend_is_available) or
        (budget >= 200)
    ):
        print("Take the trip")
    else:
        print("Stay Home")

if __name__ == "__main__":
    run()
