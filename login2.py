def create_account():
    #This function prompts the user to create a username and password for his account.
    #And also return the created username and password.
    print("Welcome to Jeffapp Account Creation!")
    while True:
        username = input("Create a username: ")
        if not username:
            print("Username cannot be empty. Please try again.")
        else:
            break

    while True:
        password = input("Create a password: ")
        if len(password) < 6:
            print("Password must be at least 6 characters long. Please try again.")
        else:
            print("Account created successfully!")
            return username,password


def login(stored_username, stored_password):
    #This fase allows the user to log in by returning True if the login was successful, False otherwise.
    #There are only three login attempts.
    print("\n--User login --")
    log_in_attempts = 0
    while log_in_attempts<3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == stored_username and password == stored_password:
            print("Log in succesfully")
            input("Welcome. What can Jeffapp do for you today?: ")
            print("Thanks for your time with Jeffapp")
            return True
        else:
            log_in_attempts += 1
            if log_in_attempts <3:
                print("Incorrect username or password. Please try again.")
                print(f"You have {3 - log_in_attempts} attempt(s) remaining.")
            else:
                print("\nYou have attempted three times.")
                print("Login denied.")
                return False
            
def main():
    #This is where we call both the create account function and the login function.
    stored_username, stored_password = create_account()
    print()
    while True:
        print("Type 'yes' if you are ready to login to Jeffapp or 'no' to cancel")
        prompt = input("Ready to log in: ").lower()


        if prompt == "yes":
            if login(stored_username, stored_password):
                print("Exiting Jeffapp. Goodbye!")
                break
            else:
                # User failed to log in after 3 attempts, so we exit.
                break
        elif prompt == "no":
            print("Login cancelled. Exiting Jeffapp.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()