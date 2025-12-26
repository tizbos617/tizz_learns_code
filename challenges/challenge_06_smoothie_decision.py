"""
Challenge 06: Smoothie Decision (3E)

Determine whether the user should drink a smoothie based on:
- hunger level
- time of day
- whether they already had a smoothie
- whether they have a health goal
"""

def run():
    hunger = input("How hungry are you? (hungry, snackish, or full): ").lower()
    time_of_day = input("What time of day is it? (morning, afternoon, or night): ").lower()
    had_smoothie = input("Have you had a smoothie? yes or no: ").lower()
    healthy_goal = input("Do you have a healthy goal? yes or no: ").lower()

    if (
        (hunger == "hungry" and time_of_day == "morning") or
        (hunger == "snackish" and not had_smoothie == "yes") or
        (healthy_goal == "yes" and time_of_day == "afternoon") or
        ((time_of_day == "night" or hunger == "full") and not had_smoothie == "yes")
    ):
        print("Drink the smoothie")
    else:
        print("Do not drink the smoothie")

if __name__ == "__main__":
    run()
