"""
Challenge 08: Smoothie Decision (Boolean Flag Version)

Determine whether the user should drink a smoothie using a boolean flag.
"""

def run():
    had_smoothie = input("Have you had a smoothie (yes or no)?: ").lower()
    had_one = (had_smoothie == "yes")

    if had_one:
        print("You should not have another one.")
    else:
        favorite_flavor = input("What is your favorite flavor?: ")
        print("You should have one.")
        print(f"You should make it a {favorite_flavor} smoothie.")

if __name__ == "__main__":
    run()
