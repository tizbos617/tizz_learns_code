import os

# ---------------------------------------------------------
# COLOR CLASS (for bold, modern, playful menu styling)
# ---------------------------------------------------------
class Color:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"


# ---------------------------------------------------------
# CLEAR SCREEN FUNCTION
# ---------------------------------------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# ---------------------------------------------------------
# IMPORT ALL CHALLENGE MODULES
# ---------------------------------------------------------
from challenges.challenge_01_gym_entry import run as gym_entry
from challenges.challenge_02_concert_entry import run as concert_entry
from challenges.challenge_03_library_checkout import run as library_checkout
from challenges.challenge_04_movie_theater_entry import run as movie_entry

from challenges.challenge_05_trip_decision import run as trip_decision
from challenges.challenge_06_smoothie_decision import run as smoothie_decision
from challenges.challenge_07_trip_decision_advanced import run as trip_advanced

from challenges.challenge_08_boolean_smoothie_flag import run as smoothie_flag
from challenges.challenge_09_boolean_gym_flag import run as gym_flag
from challenges.challenge_10_boolean_concert_flag import run as concert_flag
from challenges.challenge_11_boolean_library_flag import run as library_flag
from challenges.challenge_12_boolean_movie_flag import run as movie_flag

from challenges.challenge_13_tip_calculator import run as tip_calc
from challenges.challenge_14_uber_fare import run as uber_fare
from challenges.challenge_15_membership_pricing import run as membership_price
from challenges.challenge_16_streaming_plan import run as streaming_plan
from challenges.challenge_17_hotel_pricing import run as hotel_price
from challenges.challenge_18_car_rental import run as car_rental
from challenges.challenge_19_airline_ticket import run as airline_ticket

from challenges.challenge_20_theme_park_ticket import run as theme_park


# ---------------------------------------------------------
# MAIN MENU (bold, modern, playful)
# ---------------------------------------------------------
def main():
    while True:
        clear()
        print(Color.CYAN + "==============================================")
        print("🔥  WELCOME TO CHRIS'S CHALLENGE HUB  🔥")
        print("==============================================" + Color.RESET)
        print(Color.YELLOW + "Choose your adventure:" + Color.RESET)
        print("")
        print(Color.GREEN + "  1) Gym Entry")
        print("  2) Concert Entry")
        print("  3) Library Checkout")
        print("  4) Movie Theater Entry")
        print("  5) Trip Decision")
        print("  6) Smoothie Decision")
        print("  7) Trip Decision (Advanced)")
        print("  8) Smoothie Flag")
        print("  9) Gym Flag")
        print(" 10) Concert Flag")
        print(" 11) Library Flag")
        print(" 12) Movie Flag")
        print(" 13) Tip Calculator")
        print(" 14) Uber Fare")
        print(" 15) Membership Pricing")
        print(" 16) Streaming Plan")
        print(" 17) Hotel Pricing")
        print(" 18) Car Rental")
        print(" 19) Airline Ticket")
        print(" 20) Theme Park Ticket" + Color.RESET)
        print("")
        print(Color.RED + "  0) Exit" + Color.RESET)
        print(Color.CYAN + "==============================================" + Color.RESET)

        choice = input("\n👉 " + Color.BLUE + "Enter a number to begin: " + Color.RESET)

        if choice == "1":
            gym_entry()
        elif choice == "2":
            concert_entry()
        elif choice == "3":
            library_checkout()
        elif choice == "4":
            movie_entry()
        elif choice == "5":
            trip_decision()
        elif choice == "6":
            smoothie_decision()
        elif choice == "7":
            trip_advanced()
        elif choice == "8":
            smoothie_flag()
        elif choice == "9":
            gym_flag()
        elif choice == "10":
            concert_flag()
        elif choice == "11":
            library_flag()
        elif choice == "12":
            movie_flag()
        elif choice == "13":
            tip_calc()
        elif choice == "14":
            uber_fare()
        elif choice == "15":
            membership_price()
        elif choice == "16":
            streaming_plan()
        elif choice == "17":
            hotel_price()
        elif choice == "18":
            car_rental()
        elif choice == "19":
            airline_ticket()
        elif choice == "20":
            theme_park()
        elif choice == "0":
            clear()
            print(Color.MAGENTA + "👋 Goodbye, legend." + Color.RESET)
            break
        else:
            print(Color.RED + "\n❌ Invalid choice — try again!" + Color.RESET)
            input("Press Enter to continue...")


# ---------------------------------------------------------
# RUN PROGRAM
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
