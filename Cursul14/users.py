# Creeaza o aplicatie care permite user registration (first name, last name, user, password, email)  si user login. Datele de inregistrare se salveaza intr-un fisier .csv.
# Utilizatorul se poate loga doar daca s-a inregistrat.
# Dupa logare user-ul are posibilitatea de afisare detalii -> first name, last name, e-mail.
# Optiunea de afisare detalii nu apare inainte de logare.

import csv

file_name = "users.csv"
field_names = ["first_name", "last_name", "username", "password", "email"]
user = None

def register(first_name, last_name, username, password, email):
    if not first_name.isalpha() or not last_name.isalpha():
        print("First name and last name must be alphabetical!")
        return
    if not username.isalnum() or len(username) < 5:
        print("Username must be alphanumeric and have at least 5 characters!")
        return
    if not password.isalnum() or len(password) < 8:
        print("Password must be alphanumeric and have at least 8 characters!")
        return
    if email.count("@") != 1:
        print("Email address must contain exactly one @!")
        return
    else:
        email_name, email_domain = email.split("@")
        if len(email_name) < 5 or len(email_domain) < 5:
            print("Email name and domain must have at least 5 characters each!")
            return

    with open(file_name, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["username"] == username:
                print("Username already registered, choose another one!")
                return
            if row["email"] == email:
                print("Email already registered, choose another one!")
                return
            if row["first_name"] == first_name and row["last_name"] == last_name:
                print("You are already registered. Recovery mail sent!")
                return

    with open(file_name, 'a', newline="", encoding="utf-8") as g:
        writer = csv.DictWriter(g, fieldnames=field_names)
        writer.writerow({"first_name": first_name, "last_name": last_name, "username": username, "password": password, "email": email})
        print("User registered successfully!")

def login(username, password):
    with open(file_name, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                return row

    return None

def register_manager():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    email = input("Please enter your email: ")

    register(first_name, last_name, username, password, email)

def login_manager():
    global user
    if user is not None:
        print("You are already logged in!")
        return

    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    user = login(username, password)

    if user is None:
        print("Invalid username or password!")
    else:
        print("Login successful!")

def show_details():
    if user is not None:
        print(f"First name: {user['first_name']}, Last name: {user['last_name']}, Email: {user['email']}")
    else:
        print("You are not logged in yet!")

def logout():
    global user
    if user is not None:
        user = None
        print("Logout successful!")
    else:
        print("You are not logged in yet!")


def manager():
    print("Welcome to this app!")

    while True:
        print("Type any of the following commands:")
        print("r/R: Register")
        print("l/L: Login")
        print("d/D: Show current user details")
        print("p/P: Logout")
        print("e/E: Exit")
        user_input = input().lower()

        if user_input == "r":
            register_manager()
        elif user_input == "l":
            login_manager()
        elif user_input == "d":
            show_details()
        elif user_input == "p":
            logout()
        elif user_input == "e":
            break
        else:
            print("Invalid command!")

    print("Goodbye!")



if __name__ == '__main__':
    # register("Catalin", "Breaz", "admin", "pass1234", "catalin.brz98@yahoo.com")
    manager()