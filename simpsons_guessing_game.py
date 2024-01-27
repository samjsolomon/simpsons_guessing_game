import random
import requests

def get_api_data(api_url):
    try:
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and return the JSON data
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def check_answer(user_input, character):
    user_input_parts = user_input.lower().split()
    character_parts = character.lower().split()

    if user_input_parts == character_parts or user_input_parts[0] == character_parts[0]:
        print("CORRECT")
        return True
    else:
        print("No, sorry! It was " + character)
        return False

def play_round():
    api_url = "https://thesimpsonsquoteapi.glitch.me/quotes"
    data = get_api_data(api_url)
    if not data or 'quote' not in data[0] or 'character' not in data[0]:
        print("Failed to fetch valid data.")
        return False

    print("Who says the following quote?")
    print(f'"{data[0]["quote"]}"')
    character = data[0]['character']
    user_input = input("Name: ").strip()
    print()
    if not user_input:
        print("No, sorry! It was " + character)
        return False

    return check_answer(user_input, character)

def main():
    
    print()
    print("Welcome to the Simpsons Quote Game!")
    print("Try to guess who said the following quotes from The Simpsons.")
    print("Enter the character's name to answer.")
    print()

    score = 0
    rounds = 5  # You can adjust the number of rounds as needed

    for _ in range(rounds):
        if play_round():
            score += 1

        print(f"Your current score: {score}")
        print()
        print("----------------------------")
        print()

    print(f"Game over! Your final score: {score}")

if __name__ == "__main__":
    main()
