import requests


def get_mmr(username):
    """Function to fetch MMR data for a given username."""
    api_key = 'RGAPI-e0af80f9-e9b5-474e-b005-90f983762420'
    url = f'https://api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract MMR data from the response
        mmr = data['mmr']  # Assuming MMR data ia returned in JSON response
        return mmr
    else:
        print(f"Error fetching MMR data for {username}")
        return None


def sort_by_mmr(usernames):
    """Sort the usernames based on their MMR values."""
    sorted_usernames = sorted(usernames, key=lambda x: get_mmr(x))
    return sorted_usernames


def display_leaderboard(sorted_usernames):
    """Function to display the leaderboard."""
    print("Leaderboard: ")
    for i, username in enumerate(sorted_usernames, start=1):
        print(f"{i}. {username} - MMR: {get_mmr(username)}")


def main():
    """Main function."""
    # List of League of Legends usernames
    usernames = {'Damonides', 'Athanasy', 'OkayLoomer'}

    # Sort usernames by MMR
    sorted_usernames = sort_by_mmr(usernames)

    # Display leaderboard
    display_leaderboard(sorted_usernames)


if __name__ == '__main__':
    main()
