# Import the `datetime` module to work with dates and times
import datetime

# Define a function to calculate the user's age in years
def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Define a function to greet the user
def greet_user(name):
    print("Hello, " + name + "!")

# Define a function to ask the user for their birthdate
def get_birthdate():
    year = int(input("Enter your birth year: "))
    month = int(input("Enter your birth month (1-12): "))
    day = int(input("Enter your birth day (1-31): "))
    return datetime.date(year, month, day)

# Main program
def main():
    # Ask the user for their name
    name = input("What is your name? ")

    # Greet the user
    greet_user(name)

    # Ask the user for their birthdate
    birthdate = get_birthdate()

    # Calculate the user's age
    age = calculate_age(birthdate)

    # Print out the user's age
    print("You are " + str(age) + " years old.")

    # Ask the user if they want to play a game
    response = input("Do you want to play a game? (yes/no): ")

    # If the user wants to play a game, play a simple number guessing game
    if response.lower() == "yes":
        import random
        secret_number = random.randint(1, 100)
        guess = int(input("Guess a number between 1 and 100: "))
        while guess != secret_number:
            if guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
            guess = int(input("Guess a number between 1 and 100: "))
        print(" Congratulations! You guessed the number!")

# Run the main program
if __name__ == "__main__":
    main()