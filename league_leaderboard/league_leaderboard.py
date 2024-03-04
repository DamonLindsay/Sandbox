import requests
from summoner import Summoner

API_KEY = 'RGAPI-e0af80f9-e9b5-474e-b005-90f983762420'
REGION = 'OC1'


def main():
    """Main function."""
    # List of League of Legends usernames
    summoner_usernames = {'Damonides', 'Forlorn', 'OkayLoomer', 'FlawedDuet', 'Jordspords', 'Tardigrade', 'rourky',
                          'Cazara'}

    all_summoners = {}

    for summoner_name in summoner_usernames:
        summoner_data = get_summoner_data(REGION, summoner_name)
        if summoner_data:
            summoner = Summoner(summoner_name, summoner_data)
            all_summoners[summoner_name] = summoner
        else:
            print(f"Failed to get summoner data for {summoner_name}.")

    while True:
        print("\nMenu:")
        print("1. Display summoners sorted by level (highest to lowest)")
        print("2. Display summoners sorted by name (alphabetical)")
        print("3. Display summoner data SECRET")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_summoners_sorted_by_level(all_summoners)
        elif choice == "2":
            display_summoners_sorted_by_name(all_summoners)
        elif choice == "3":
            command = input("Enter command in format '!dev SummonerName': ")
            if command.startswith("!dev "):
                summoner_name = command[5:]
                display_summoner_data(all_summoners, summoner_name)
        elif choice == "4":
            exit_program()
            break
        else:
            print("Invalid choice.  Please try again.")


def display_summoners_sorted_by_level(all_summoners):
    """Display summoners sorted by level."""
    sorted_summoners = sorted(all_summoners.values(), key=lambda x: x.summoner_level, reverse=True)
    print("\nSummoners sorted by level (highest to lowest):")
    for summoner in sorted_summoners:
        print(f"{summoner.name}: Level {summoner.summoner_level}")


def display_summoners_sorted_by_name(all_summoners):
    """Display summoners sorted by name."""
    sorted_summoners = sorted(all_summoners.values(), key=lambda x: x.name)
    print("\nSummoners sorted by name (alphabetical):")
    for summoner in sorted_summoners:
        print(f"{summoner.name}: Level {summoner.summoner_level}")


def display_summoner_data(all_summoners, summoner_name):
    if summoner_name in all_summoners:
        summoner = all_summoners[summoner_name]
        print(f"\nSummoner data for {summoner_name}:")
        print(f"Name: {summoner_name}")
        print(f"Summoner Level: {summoner.summoner_level}")
        print(f"ID: {summoner.id}")
        print(f"Account ID: {summoner.account_id}")
        print(f"PUUID: {summoner.puuid}")
        print(f"Profile Icon ID: {summoner.profile_icon_id}")
        print(f"Revision Date: {summoner.revision_date}")
    else:
        print(f"Summoner {summoner_name} not found.")


def exit_program():
    print("Exiting...")


def get_summoner_data(region, summoner_name):
    """Gets all the summoners data."""
    url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        summoner_data = response.json()
        return summoner_data
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving summoner data for {summoner_name}: {e}")
        return None


if __name__ == '__main__':
    main()
