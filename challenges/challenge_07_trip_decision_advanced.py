"""
Challenge 07: Trip Decision (Advanced)

A more complex version of the trip decision challenge using:
- weather
- gas level
- friend availability
- budget
- OR/AND combinations
"""

def run():
    weather = input("What will the weather be like? ").lower()
    gas = int(input("How much gas do you have? "))
    friend = input("Do you have a friend to join you? ").lower()
    has_friend = (friend == "yes")
    budget = int(input("How much money do you have? "))

    if (
        (weather == "sunny" and gas >= 50) or
        (budget >= 150 and has_friend) or
        ((weather == "cloudy" or gas >= 75) and not has_friend) or
        (budget >= 300)
    ):
        print("Take the trip")
    else:
        print("Do not take the trip")

if __name__ == "__main__":
    run()
