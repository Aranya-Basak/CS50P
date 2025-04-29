import requests
import json
import random
from datetime import datetime, timezone
from tabulate import tabulate
from colorama import Fore, Style

api_url = "https://ll.thespacedevs.com/2.2.0/launch/upcoming/"
favorite_agencies = []


def fetch_launches():
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data["results"]
    except requests.RequestException:
        print(
            Fore.RED + "Error fetching launch data. Trying offline..." + Style.RESET_ALL
        )
        return []


def save_launches_offline(launches, filename="launches.json"):
    with open(filename, "w") as file:
        json.dump(launches, file)


def load_launches_offline(filename="launches.json"):
    try:
        with open(filename, "r") as file:
            launches = json.load(file)
            print(Fore.YELLOW + "loaded offline launch data." + Style.RESET_ALL)
            return launches
    except FileNotFoundError:
        print(Fore.RED + "No offline data" + Style.RESET_ALL)
        return []


def show_menu():
    print(Fore.CYAN + "\n=== Space Mission Tracker ===" + Style.RESET_ALL)
    print("1. Show upcoming launches")
    print("2. Filter launches by agency")
    print("3. Search launches by date")
    print("4. Countdown to next launch")
    print("5. Sort launches by date")
    print("6. Add favoritte agency")
    print("7. Show launches from favorites")
    print("8. Filter launches by country")
    print("9. Random launch of the day")
    print("10. Exit")
    choice = input("Select an option(1-10): ")
    return choice


def show_upcoming_launches(launches):
    table = []
    for launch in launches:
        name = launch["name"]
        date = launch["net"]
        agency = launch["launch_service_provider"]["name"]
        table.append([name, date, agency])

    headers = ["Mission", "Launch Date", "Agency"]
    print(tabulate(table, headers, tablefmt="fancy_grid"))


def filter_launches_by_agency(launches):
    agency_name = input("Enter the agency name: ").lower()
    filtered_name = [
        launch
        for launch in launches
        if agency_name in launch["launch_service_provider"]["name"].lower()
    ]
    if filtered_name:
        show_upcoming_launches(filtered_name)
    else:
        print(Fore.YELLOW + "No launches found for that agency." + Style.RESET_ALL)


def search_launches_by_date(launches):
    date_input = input("Enter a date (YYYY-MM-DD): ")
    try:
        target_date = datetime.strptime(date_input, "%Y-%m-%d").date()
        matches = []

        for launch in launches:
            launch_date_str = launch["net"]
            launch_date = datetime.strptime(
                launch_date_str.split("T")[0], "%Y-%m-%d"
            ).date()

            if launch_date == target_date:
                matches.append(launch)

        if matches:
            show_upcoming_launches(matches)
        else:
            print(Fore.YELLOW + "No launches found on that date." + Style.RESET_ALL)

    except ValueError:
        print(Fore.RED + "Invalid dat format. Please use YYYY-MM-DD." + Style.RESET_ALL)


def countdown_to_next_launch(launches):
    if not launches:
        print("No upcoming launch.")
        return

    launches = sorted(launches, key=lambda x: x["net"])
    next_launch = launches[0]
    launch_time_str = next_launch["net"]
    launch_time = datetime.strptime(launch_time_str, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=timezone.utc
    )

    now = datetime.now(timezone.utc)
    time_left = launch_time - now
    if time_left.total_seconds() <= 0:
        days, hours, minutes = 0, 0, 0
    else:
        days = time_left.days
        hours, reminder = divmod(time_left.seconds, 3600)
        minutes, _ = divmod(reminder, 60)

    print(
        Fore.MAGENTA
        + f"\nNext Launch: {next_launch["name"]} ({next_launch['launch_service_provider']['name']})"
    )
    print(
        f"Time left: {days} days, {hours} hours, {minutes} minutes\n" + Style.RESET_ALL
    )


def sort_launches_by_date(launches):
    order = input("Sort by (1) Soonest or (2) Latest? ").strip()
    sorted_launches = sorted(
        launches,
        key=lambda l: datetime.strptime(l["net"], "%Y-%m-%dT%H:%M:%SZ"),
        reverse=(order == "2"),
    )
    show_upcoming_launches(sorted_launches)


def add_favorite_agency():
    agency = input("Enter Agency name to add to favorites: ")
    if agency:
        favorite_agencies.append(agency.lower())
        print(Fore.GREEN + f"{agency} added to favorites." + Style.RESET_ALL)


def show_launches_from_favorites(launches):
    if not favorite_agencies:
        print(Fore.YELLOW + "No favorite agencies added yet." + Style.RESET_ALL)

    favorites = [
        launch
        for launch in launches
        if launch["launch_service_provider"]["name"].lower() in favorite_agencies
    ]

    if favorites:
        show_upcoming_launches(favorites)
    else:
        print(
            Fore.YELLOW + "No upcoming launches form your favorites" + Style.RESET_ALL
        )


def filter_launches_by_country(launches):
    country = input("Enter a country code (e.g. USA, RUS, CHN): ").lower()
    filtered = [
        launch
        for launch in launches
        if country
        in launch.get("pad", {}).get("location", {}).get("country_code", "").lower()
    ]

    if filtered:
        show_upcoming_launches(filtered)
    else:
        print(Fore.YELLOW + "No launches found for that country." + Style.RESET_ALL)


def random_launch_of_the_day(launches):
    if launches:
        launch = random.choice(launches)
        print(Fore.BLUE + f"\nRandom Launch Pick:" + Style.RESET_ALL)
        show_upcoming_launches([launch])
    else:
        print("No launches available.")


def main():
    launches = fetch_launches()

    if not launches:
        launches = load_launches_offline()
    else:
        save_launches_offline(launches)

    if not launches:
        return

    while True:
        choice = show_menu()

        if choice == "1":
            show_upcoming_launches(launches)
        elif choice == "2":
            filter_launches_by_agency(launches)
        elif choice == "3":
            search_launches_by_date(launches)
        elif choice == "4":
            countdown_to_next_launch(launches)
        elif choice == "5":
            sort_launches_by_date(launches)
        elif choice == "6":
            add_favorite_agency()
        elif choice == "7":
            show_launches_from_favorites(launches)
        elif choice == "8":
            filter_launches_by_country(launches)
        elif choice == "9":
            random_launch_of_the_day(launches)
        elif choice == "10":
            print(
                Fore.GREEN + "Goodbye, and keep looking to the stars!" + Style.RESET_ALL
            )
            break
        else:
            print(Fore.RED + "Invalid option. Please select 1-10." + Style.RESET_ALL)


if __name__ == "__main__":
    main()